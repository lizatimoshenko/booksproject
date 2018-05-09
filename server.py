from os import getenv
from bottle import get, post, redirect, request, route, run, static_file, view, template, TEMPLATE_PATH, response, abort
from py2neo import Graph, watch, authenticate
from os.path import dirname, join as path_join
# from py2neo.neo4j import GraphDatabaseService, CypherQuery
import bcrypt
from pandas import DataFrame
from models import User, Book

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


@route("/register")
def get_form():
    return static_file("register.html", root="views")


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
    graph.push(user)
    redirect("/")


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

            book = graph.run("MATCH (b:Book) RETURN b").data()
            book_data = book[0].get('b')
            info = {'username': username,
                    'image': book_data['image'],
                    'title': book_data['title']}
            print()
            return template('profile.tpl', info)
        else:
            return "<p>Login failed.</p>"


@route("/login")
def get_home():
    username = request.get_cookie("account", secret='some-secret-key')
    info = {'username': username}
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
    info = {'username': user_data['username'],
            'email': user_data['email'],
            'name': user_data['name'],
            'surname': user_data['surname']}
    return template('settings.tpl', info)


@route("/following")
def following():
    username = request.get_cookie("account", secret='some-secret-key')
    info = {'username': username}
    return template('followings.tpl', info)


@route("/searchpeople")
def following():
    username = request.get_cookie("account", secret='some-secret-key')
    users = graph.run("MATCH (user:User) WHERE user.username <> {N} RETURN user", {"N": username}).data()
    usernames = []
    for user in users:
        usernames.append(user['user']['username'])

    info = {'username': username,
            'usernames': usernames}

    return template('searchpeople.tpl', info)


@route("/followers")
def followers():
    username = request.get_cookie("account", secret='some-secret-key')
    followers = graph.run("MATCH (u:User)-[:FOLLOWS]->(f:User {username:{F}})"
                          "RETURN u", {"F": username}).data()
    print(followers)
    usernames = []
    for follower in followers:
        usernames.append(follower['u']['username'])

    info = {'username': username,
            'usernames': usernames}

    return template('followerspage.tpl', info)


@route("/follow/<user>")
def following(user):
    username = request.get_cookie("account", secret='some-secret-key')
    graph.run("MATCH (u:User {username:{U}}),(f:User {username:{F}})"
              "MERGE (u)-[:FOLLOWS]->(f)", {"U": username, "F": user})
    users = graph.run("MATCH (user:User) WHERE user.username <> {N} RETURN user", {"N": username}).data()
    usernames = []
    for user in users:
        usernames.append(user['user']['username'])

    info = {'username': username,
            'usernames': usernames}

    return template('searchpeople.tpl', info)


@route("/read_more/<title>")
def read_more(title):
    username = request.get_cookie("account", secret='some-secret-key')
    book = graph.run("MATCH (book:Book) WHERE book.title={N} RETURN book", {"N": title}).data()
    book_data = book[0].get('book')

    info = {'title': book_data['title'],
            'image': book_data['image'],
            'language': book_data['language'],
            'published': book_data['published'],
            'annotation': book_data['annotation'],
            'username': username}

    return template('read_more.tpl', info)

# Static CSS Files
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


def server_static_img(filename):
    return static_file(filename, root='/static/images')


def server_static_js(filename):
    return static_file(filename, root='/static/js')


run(host='localhost', port=8080, debug=True)
