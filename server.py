import bottle
from bottle import get, post, redirect, request, route, run, static_file, view, template, TEMPLATE_PATH, response, abort
from py2neo import Graph, watch, authenticate, remote
from os.path import dirname, join as path_join
import os
import bcrypt
from models import User
from beaker.middleware import SessionMiddleware
home = dirname(__file__)
static = path_join(home, "static")
TEMPLATE_PATH.insert(0, path_join(home, "views"))

authenticate("localhost:7474", "neo4j", "")
salt = bcrypt.gensalt()

# Set up a link to the local graph database.
graph = Graph("http://localhost:7474/db/data/")
watch("neo4j.bolt")

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@route("/")
def get_index():
    """ Index page.
    """
    return static_file("index.html", root="views")


@route("/register", method='POST')
def get_register():
    """"""
    user = User()
    username = request.forms.get('name')
    user.email = request.forms.get('email')
    hashed = bcrypt.hashpw(request.forms.get('password').encode('utf-8'), salt)

    check_if_user_exist = graph.run("MATCH (user {username:{N}}) RETURN user.username, user.email",
                                    {"N": username}).data()

    user.username = username
    user.password = hashed
    image = "./static/images/images.jpeg"
    user.image = image
    graph.push(user)

    info = {'username': username,
            'avatar': image,
            'image': '',
            'title': ''}

    return template('profile.tpl', info)


# TODO  if username exist show it to user

@route("/login", method="POST")
def get_login():
    username = request.forms.get('name')
    user_password = graph.run("MATCH (user {username:{N}}) RETURN user.password,user.username", {"N": username}).data()
    if len(user_password) == 0:
        return "<p>User not found</p>"
    else:

        password = request.forms.get('password')
        if bcrypt.checkpw(password, str(user_password[0]['user.password'])):
            response.set_cookie("account", username, secret='some-secret-key')
            user = graph.run("MATCH (u:User {username:{U}}) RETURN u", {"U": username}).data()
            user_data = user[0].get('u')

            # last added
            last_added_books = graph.run("MATCH (b:Book) RETURN b ORDER BY b.added_at LIMIT 4")

            list_of_last_added_books = []

            while last_added_books.forward():
                data = last_added_books.current()["b"]
                list_of_last_added_books.append(dict(data))
            print(list_of_last_added_books)
            info = {'username': username,
                    'avatar': user_data['image'],
                    'last_added_books': list_of_last_added_books}

            result = graph.run("MATCH (u:User {username:{F}})-[:FOLLOWS]->(follower:User)"
                               "-[:READ]->(book:Book)"
                               "RETURN DISTINCT book", {"F": username})

            user_books = []

            while result.forward():
                book = result.current()["book"]
                user_books.append(book)

            result1 = graph.run("MATCH (u:User {username:{F}})<-[:FOLLOWS]-(follower:User)"
                                "-[:READ]->(book:Book)"
                                "RETURN DISTINCT book", {"F": username})

            user_books1 = []

            while result1.forward():
                book = result1.current()["book"]
                user_books1.append(book)

            info = {'username': username,
                    'avatar': user_data['image'],
                    'last_added_books': list_of_last_added_books,
                    'user_books': user_books,
                    'user_books1': user_books1}

            return template('profile.tpl', info)
        else:
            return "<p>Login failed.</p>"


@route("/login")
def get_home():
    username = request.get_cookie("account", secret='some-secret-key')
    user = graph.run("MATCH (u:User {username:{U}}) RETURN u", {"U": username}).data()
    user_data = user[0].get('u')
    # last added
    last_added_books = graph.run("MATCH (b:Book) RETURN b ORDER BY b.added_at LIMIT 4")

    list_of_last_added_books = []

    while last_added_books.forward():
        data = last_added_books.current()["b"]
        list_of_last_added_books.append(dict(data))

    result = graph.run("MATCH (u:User {username:{F}})-[:FOLLOWS]->(follower:User)"
                       "-[:READ]->(book:Book)"
                       "RETURN DISTINCT book", {"F": username})

    user_books = []

    while result.forward():
        book = result.current()["book"]
        user_books.append(book)

    result1 = graph.run("MATCH (u:User {username:{F}})<-[:FOLLOWS]-(follower:User)"
                       "-[:READ]->(book:Book)"
                       "RETURN DISTINCT book", {"F": username})

    user_books1 = []

    while result1.forward():
        book = result1.current()["book"]
        user_books1.append(book)

    info = {'username': username,
            'avatar': user_data['image'],
            'last_added_books': list_of_last_added_books,
            'user_books': user_books,
            'user_books1': user_books1}

    return template("profile.tpl", info)


@route("/logout")
def log_out():
    response.set_cookie('auto', '')
    redirect('/')


@route("/settings")
def settings():
    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    genre_nodes = graph.run("MATCH (g:Genre) RETURN g")
    genres = []
    while genre_nodes.forward():
        genre = genre_nodes.current()["g"]
        genres.append(genre['name'])

    info = {'username': user_data['username'],
            'email': user_data['email'],
            'name': user_data['name'],
            'surname': user_data['surname'],
            'avatar': user_data['image'],
            'genres': genres,
            'preferences': None
            }
    preferences = user_data['preferences']
    if preferences is not None:
        list_of_preferences = preferences.split(",")
        info['preferences'] = list_of_preferences

    return template('settings.tpl', info)


@route("/following")
def following():
    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (u:User {username:{F}})-[:FOLLOWS]->(following:User)"
                       "-[:READ]->(book:Book)"
                       "RETURN following, collect(book) as books", {"F": username})

    users = []
    user_books = {}

    while result.forward():
        user = result.current()["following"]
        users.append(user)

        books = result.current()["books"]
        user_books[user['username']] = books

    info = {'username': username,
            'avatar': user_data['image'],
            'users': users,
            'user_books': user_books}

    return template('followings.tpl', info)


@route("/searchpeople")
def following():
    username = request.get_cookie("account", secret='some-secret-key')
    result = graph.run("MATCH (user:User)"
                       "WHERE (NOT (user)<-[:FOLLOWS]-(:User {username:{N}})) "
                       "AND user.username<>{N}"
                       "RETURN user", {"N": username})

    users = []
    if result.data() is not None:
        while result.forward():
            data = result.current()["user"]
            users.append(dict(data))

    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    info = {'username': username,
            'users': users,
            'avatar': user_data['image']}

    return template('searchpeople.tpl', info)


@route("/followers")
def followers():
    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')
    result = graph.run("MATCH (user:User)-[:FOLLOWS]->(f:User {username:{F}})"
                       "RETURN user", {"F": username})


    users = []

    while result.forward():
        data = result.current()["user"]
        users.append(dict(data))

    print(users)

    followings_res = graph.run("MATCH (u:User {username:{F}})-[:FOLLOWS]->(following:User)"
                               "RETURN following", {"F": username})

    followings = []

    while followings_res.forward():
        data = followings_res.current()['following']
        followings.append(data['username'])

    result = graph.run("MATCH (u:User {username:{F}})<-[:FOLLOWS]-(follower:User)"
                       "-[:READ]->(book:Book)"
                       "RETURN follower, collect(book) as books", {"F": username})

    users = []
    user_books = {}

    while result.forward():
        user = result.current()["follower"]
        users.append(user)

        books = result.current()["books"]
        user_books[user['username']] = books


    info = {'username': username,
            'users': users,
            'avatar': user_data['image'],
            'followings': followings,
            'user_books': user_books
            }

    return template('followerspage.tpl', info)


@route("/follow", method="POST")
def following():
    username = request.get_cookie("account", secret='some-secret-key')


    # get following user
    follow = request.POST['user']
    print(follow)
    # create a relationship

    graph.run("MATCH (u:User {username:{U}}),(f:User {username:{F}})"
              "MERGE (u)-[:FOLLOWS]->(f)", {"U": username, "F": follow})

    redirect("/search_followings")


@route("/unfollow", method="POST")
def unfollow_user():
    username = request.get_cookie("account", secret='some-secret-key')

    # get current user data
    user = graph.run("MATCH (u:User {username:{U}}) RETURN u", {"U": username}).data()
    user_data = user[0].get('u')

    # get following user
    unfollow = request.POST['user']
    print(unfollow)
    # create a relationship
    graph.run("MATCH (u:User {username:{U}})-[r:FOLLOWS]->(f:User {username:{F}})"
              "DELETE r", {"U": username, "F": unfollow})

    # find other users
    result = graph.run("MATCH (users:User)<-[:FOLLOWS]-(user:User {username:{N}})"
                       "RETURN users", {"N": username})

    # extract users data
    users = []
    while result.forward():
        data = result.current()["users"]
        users.append(dict(data))

    info = {'username': username,
            'users': users,
            'avatar': user_data['image']
            }

    return "Done"


@route("/read_more")
def read_more():
    username = request.get_cookie("account", secret='some-secret-key')
    book_title = request.query.title

    print(book_title)
    book = graph.run("MATCH (book:Book) WHERE book.title={N}"
                     "RETURN book", {"N": book_title}).data()
    authors = graph.run("MATCH (author:Author)-[:WROTE]->(book:Book {title:{N}})"
                        "RETURN author", {"N": book_title}).data()
    genres = graph.run("MATCH (genre:Genre)-[:GENRE_OF]->(book:Book {title:{N}})"
                       "RETURN genre", {"N": book_title})
    genres_list = []
    while genres.forward():
        data = genres.current()['genre']
        genres_list.append(dict(data))

    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    book_info = book[0].get('book')
    author = authors[0].get('author')
    info = {'username': username,
            'avatar': user_data['image'],
            'book_info': book_info,
            'author': author['name'],
            'genres': genres_list
            }

    return template('aboutbook.tpl', info)


@route("/about_author")
def about_author():
    username = request.get_cookie("account", secret='some-secret-key')
    name = request.query.author
    authors = graph.run("MATCH (author:Author {name:{N}})"
                        "RETURN author", {"N": name}).data()
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    books = graph.run("MATCH (author:Author {name:{N}})-[:WROTE]->(book:Book)"
                      "RETURN book", {"N": name})

    books_list = []
    while books.forward():
        data = books.current()['book']
        books_list.append(dict(data))

    author = authors[0].get('author')
    info = {'name': author['name'],
            'image': author['image'],
            'born': author['born'],
            'username': username,
            'avatar': user_data['image'],
            'books': books_list}

    return template('author_page.tpl', info)


@route("/subscribe_author", method="POST")
def subscribe_author():
    data = request.json
    name = data['name']
    username = request.get_cookie("account", secret='some-secret-key')
    graph.run("MATCH (user:User {username:{U}}),"
              "(author:Author {name:{A}})"
              "MERGE (user)-[:LIKES]->(author)",
              {"A": name, "U": username})

    return "Done"


@route("/unsubscribe_author", method="POST")
def unsubscribe_author():
    data = request.json
    name = data['name']
    username = request.get_cookie("account", secret='some-secret-key')
    graph.run("MATCH (user:User {username:{U}})-[r:LIKES]->(author:Author {name:{A}})"
              "DELETE r ",
              {"A": name, "U": username})

    return "Done"


@route("/add_wish", method="POST")
def add_wish():
    data = request.json
    title = data['title']
    username = request.get_cookie("account", secret='some-secret-key')
    graph.run("MATCH (user:User {username:{U}}),"
              "(book:Book {title:{B}})"
              "MERGE (user)-[:WISHES]->(book)",
              {"B": title, "U": username})

    return "Done"


@route("/delete_wish", method="POST")
def delete_wish():
    data = request.json
    title = data['title']
    username = request.get_cookie("account", secret='some-secret-key')
    graph.run("MATCH (user:User {username:{U}})-[r:WISHES]->(book:Book {title:{B}})"
              "DELETE r ",
              {"B": title, "U": username})

    return "Done"


@route("/unread_book", method="POST")
def unread_book():
    data = request.json
    title = data['title']
    username = request.get_cookie("account", secret='some-secret-key')
    graph.run("MATCH (user:User {username:{U}})-[r:READ]->(book:Book {title:{B}})"
              "DELETE r ",
              {"B": title, "U": username})

    return "Done"


@route("/read_book", method="POST")
def read_book():
    data = request.json
    title = data['title']
    username = request.get_cookie("account", secret='some-secret-key')


    graph.run("MATCH (user:User {username:{U}}),"
              "(book:Book {title:{B}})"
              "MERGE (user)-[:READ]->(book)",
              {"B": title, "U": username})

    return "Done"


@route("/wishlist")
def add_wish():
    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (u:User {username:{U}})-[:WISHES]->(book)"
                      "RETURN book", {"U": username})

    books = []

    while result.forward():
        data = result.current()['book']
        books.append(dict(data))

    info = {'username':username,
            'avatar': user_data['image'],
            'books':books
            }

    return template('wishlist.tpl', info)


@route("/books")
def books_list():
    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (u:User {username:{U}})-[:READ]->(book)"
                       "RETURN book", {"U": username})

    books = []

    while result.forward():
        data = result.current()['book']
        books.append(dict(data))

    info = {'username': username,
            'avatar': user_data['image'],
            'books': books
            }

    return template('books.tpl', info)


@route('/change_personal_information', method='POST')
def personal_information():
    username = request.get_cookie("account", secret='some-secret-key')
    user_image_path = graph.run("MATCH (user:User {username:{U}})"
                                "RETURN user.image", {"U": username}).data()
    file = user_image_path[0]['user.image']
    print(file)

    data = request.POST
    upload = data['file']
    print(upload)
    print(type(upload))
    if type(upload) == bottle.FileUpload:
        print("Yes")
        if file is not None:
            print("File exists.")
            path, file = os.path.split(os.path.abspath(file))
            print("Path=", path)
            print("File=", file)
            os.remove(path + "/" + file)
            print("Previous file deleted.")

        filename, ext = os.path.splitext(upload.filename)
        if ext not in ('.png', '.jpg', '.jpeg'):
            return "File extension not allowed."

        save_path = "static/images"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        file_path = "./{path}/{file}".format(path=save_path, file=upload.filename)
        upload.save(file_path)
        graph.run("MATCH (user:User {username:{U}})"
                  "SET user.image = {F}", {"U": username, "F": file_path})

    name = data['name']
    surname = data['surname']

    if name is not None:
        graph.run("MATCH (user:User {username:{U}})"
                  "SET user.name= {F}", {"U": username, "F": name})
    if surname is not None:
        graph.run("MATCH (user:User {username:{U}})"
                  "SET user.surname= {F}", {"U": username, "F": surname})

    return "Done"


@route("/change_account_info", method="POST")
def change_account_info():
    username = request.get_cookie("account", secret='some-secret-key')
    data = request.POST
    email = data['email']
    password = data['password']
    confirm = data['confirm']

    if (password is None) and (confirm is None):
        graph.run("MATCH (user:User {username:{U}})"
                  "SET user.email = {E} ",
                  {"E": email, "U": username})
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        graph.run("MATCH (user:User {username:{U}})"
                  "SET user.email = {E},"
                  "user.password = {P}",
                  {"E": email, "U": username, "P": hashed_password})
    return "Done"


@route("/add_preferences", method="POST")
def add_preferences():
    username = request.get_cookie("account", secret='some-secret-key')
    data = request.POST
    preferences = data['preferences']

    graph.run("MATCH (user:User {username:{U}})"
              "SET user.preferences = {P}",
              {"U": username, "P": preferences})

    return "Done"


# Static CSS Files
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


def server_static_img(filename):
    return static_file(filename, root='/static/images')


def server_static_js(filename):
    return static_file(filename, root='/static/js')


@route('/search_followings')
def search():

    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (user:User)"
                       "WHERE user.name<>{U}"
                       "RETURN user", {"U": username})

    followings_res = graph.run("MATCH (u:User {username:{F}})-[:FOLLOWS]->(following:User)"
                               "RETURN following", {"F": username})

    users = []

    while result.forward():
        data = result.current()['user']
        users.append(dict(data))

    followings = []

    while followings_res.forward():
        data = followings_res.current()['following']
        followings.append(data['username'])

    result = graph.run("MATCH (user:User)-[:READ]->(book:Book)"
                       "WHERE (user.username<>{U})"
                       "RETURN user, collect(book) as books", {"U": username})


    user_books = {}

    while result.forward():
        user = result.current()["user"]
        books = result.current()["books"]
        user_books[user['username']] = books

    info = {'username': username,
            'avatar': user_data['image'],
            'users': users,
            'followings': followings,
            'user_books': user_books}

    return template('searchresult.tpl', info)


@route('/search_followings', method="POST")
def search():
    res = request.forms.get('search')

    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (user:User)-[:READ]->(book:Book)"
                       "WHERE (user.username CONTAINS {Q})"
                       "AND (user.username<>{U})"
                       "RETURN user, collect(book) as books", {"U": username, "Q":res})

    users = []
    user_books = {}

    while result.forward():
        user = result.current()["user"]
        users.append(user)

        books = result.current()["books"]
        user_books[user['username']] = books

    followings_res = graph.run("MATCH (u:User {username:{F}})-[:FOLLOWS]->(following:User)"
                               "RETURN following", {"F": username})

    followings = []

    while followings_res.forward():
        data = followings_res.current()['following']
        followings.append(data['username'])
    print(followings)
    info = {'username': username,
            'avatar': user_data['image'],
            'users': users,
            'followings': followings,
            'user_books': user_books}

    return template('searchresult.tpl', info)


@route("/authors")
def show_authors():
    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (u:User {username:{F}})-[:LIKES]->(author:Author)"
                       "-[:WROTE]->(book:Book)"
                       "RETURN author,collect(book) as books", {"F": username})


    authors = []

    user_books = {}

    while result.forward():
        author = result.current()["author"]
        authors.append(author)

        books = result.current()["books"]
        user_books[author['name']] = books

    info = {'username': username,
            'avatar': user_data['image'],
            'authors': authors,
            'user_books': user_books}

    return template('authors.tpl', info)


@route('/search_authors', method="POST")
def search_authors():
    res = request.forms.get('search')
    print(res)
    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (author:Author)"
                       "WHERE (author.name CONTAINS {Q})"
                       "RETURN author", {"Q": res, "U": username})

    print(result)


    authors = []

    while result.forward():
        data = result.current()['author']
        authors.append(dict(data))

    likes = []

    info = {'username': username,
            'avatar': user_data['image'],
            'authors': authors}

    return template('authorsearch.tpl', info)


bottle.run(host='localhost', port=8080, debug=True)
