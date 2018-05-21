import bottle
from bottle import get, post, redirect, request, route, run, static_file, view, template, TEMPLATE_PATH, response, abort
from py2neo import Graph, watch, authenticate
from os.path import dirname, join as path_join
import os
import bcrypt
from models import User
import json
home = dirname(__file__)
static = path_join(home, "static")
TEMPLATE_PATH.insert(0, path_join(home, "views"))

authenticate("localhost:7474", "neo4j", "")
salt = bcrypt.gensalt()

# Set up a link to the local graph database.
graph = Graph("http://localhost:7474/db/data/")
watch("neo4j.bolt")


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
            book = graph.run("MATCH (b:Book) RETURN b").data()
            book_data = book[0].get('b')
            info = {'username': username,
                    'avatar': user_data['image'],
                    'image': book_data['image'],
                    'title': book_data['title']}
            print()
            return template('profile.tpl', info)
        else:
            return "<p>Login failed.</p>"


@route("/login")
def get_home():
    username = request.get_cookie("account", secret='some-secret-key')
    book = graph.run("MATCH (b:Book) RETURN b").data()
    book_data = book[0].get('b')
    user = graph.run("MATCH (u:User {username:{U}}) RETURN u", {"U": username}).data()
    user_data = user[0].get('u')
    info = {'username': username,
            'avatar': user_data['image'],
            'image': book_data['image'],
            'title': book_data['title']}
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

    followings = graph.run("MATCH (u:User {username:{F}})-[:FOLLOWS]->(following:User)"
                           "RETURN following", {"F": username})

    users = []

    while followings.forward():
        data = followings.current()["following"]
        users.append(dict(data))

    info = {'username': username,
            'avatar': user_data['image'],
            'users': users}

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
    followers = graph.run("MATCH (u:User)-[:FOLLOWS]->(f:User {username:{F}})"
                          "RETURN u", {"F": username}).data()

    usernames = []
    for follower in followers:
        usernames.append(follower['u']['username'])

    info = {'username': username,
            'usernames': usernames}

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


@route("/read_more/<title>")
def read_more(title):
    username = request.get_cookie("account", secret='some-secret-key')
    book = graph.run("MATCH (book:Book) WHERE book.title={N} RETURN book", {"N": title}).data()
    book_data = book[0].get('book')
    authors = graph.run("MATCH (author:Author)-[:WROTE]->(book:Book {title:{N}})"
                        "RETURN author", {"N": title}).data()
    author_name = authors[0].get('author')
    info = {'title': book_data['title'],
            'image': book_data['image'],
            'language': book_data['language'],
            'published': book_data['published'],
            'annotation': book_data['annotation'],
            'username': username,
            'author': author_name['name']}
    print(info)
    return template('read_more.tpl', info)


@route("/about_author/<name>")
def about_author(name):
    username = request.get_cookie("account", secret='some-secret-key')

    authors = graph.run("MATCH (author:Author {name:{N}})"
                        "RETURN author", {"N": name}).data()
    author = authors[0].get('author')
    info = {'name': author['name'],
            'image': author['image'],
            'born': author['born'],
            'username': username}
    print(info)
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
    books = graph.run("MATCH (u:User {username:{U}})-[:WISHES]->(book)"
                      "RETURN book", {"U": username}).data()
    book_data = books[0].get('book')

    info = {'title': book_data['title'],
            'image': book_data['image'],
            'language': book_data['language'],
            'published': book_data['published'],
            'annotation': book_data['annotation'],
            'username': username}

    return template('wishlist.tpl', info)


@route("/books")
def books_list():
    username = request.get_cookie("account", secret='some-secret-key')
    books = graph.run("MATCH (u:User {username:{U}})-[:READ]->(book)"
                      "RETURN book", {"U": username}).data()
    book_data = books[0].get('book')

    info = {'title': book_data['title'],
            'image': book_data['image'],
            'language': book_data['language'],
            'published': book_data['published'],
            'annotation': book_data['annotation'],
            'username': username}

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

    users = []

    while result.forward():
        data = result.current()['user']
        users.append(dict(data))

    info = {'username': username,
            'avatar': user_data['image'],
            'users': users}

    return template('searchresult.tpl', info)


@route('/search_followings', method="POST")
def search():
    res = request.forms.get('search')

    username = request.get_cookie("account", secret='some-secret-key')
    user_info = graph.run("MATCH (user {username:{N}}) RETURN user", {"N": username}).data()
    user_data = user_info[0].get('user')

    result = graph.run("MATCH (user:User)"
                       "WHERE (user.username CONTAINS {Q})"
                       "AND (user.username<>{U})"
                       "RETURN user", {"Q": res, "U": username})

    users = []

    while result.forward():
        data = result.current()['user']
        users.append(dict(data))

    info = {'username': username,
            'avatar': user_data['image'],
            'users': users}

    return template('searchresult.tpl', info)




run(host='localhost', port=8080, debug=True)
