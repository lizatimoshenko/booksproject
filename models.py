from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom


class User(GraphObject):
    __primarykey__ = 'username'

    # fields for registration
    username = Property()
    email = Property()
    password = Property()

    # additional fields for profile
    name = Property()
    username = Property()
    preferences = Property()
    gender = Property()

    # relationships
    follow = RelatedTo("User")
    read = RelatedTo("Book")
    wrote = RelatedTo("Review")
    subscribe = RelatedTo("Author")
    prefer = RelatedTo("Genre")


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


class Author(GraphObject):
    __primarykey__ = 'name' #???

    name = Property()
    biography = Property()

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





