from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom


class User(GraphObject):
    __primarykey__ = 'username'

    # fields for registration
    username = Property()
    email = Property()
    password = Property()

    # additional fields for profile
    name = Property()
    surname = Property()
    preferences = Property()
    image = Property()

    # relationships
    follow = RelatedTo("User")
    read = RelatedTo("Book")
    wrote = RelatedTo("Review")
    subscribe = RelatedTo("Author")
    prefer = RelatedTo("Genre")
    wishes = RelatedTo("Book")
    follower = RelatedFrom("User", "FOLLOWS")


class Book(GraphObject):
    __primarykey__ = 'title'

    title = Property()
    published = Property()
    annotation = Property()
    language = Property()
    image = Property() #how to store images
    plot_tags = Property("plottags")

    # relationships
    author = RelatedFrom("Author", "WROTE")
    genre = RelatedFrom("Genre", "IS_GENRE")
    reader = RelatedFrom("User", "READ")
    review = RelatedFrom("Review", "ABOUT")
    wish = RelatedFrom("User", "WISHES")


class Author(GraphObject):
    __primarykey__ = 'name' #???

    name = Property()
    born = Property()

    wrote = RelatedTo(Book)
    liked = RelatedFrom("User", "SUBSCRIBE")


class Genre(GraphObject):
    __primarykey__ = 'name'

    name = Property()
    description = Property()

    preferred = RelatedFrom("User", "PREFER")


class Review(GraphObject):

    text = Property()

    author = RelatedFrom("User", "WROTE")
    about = RelatedTo("Book", "ABOUT")





