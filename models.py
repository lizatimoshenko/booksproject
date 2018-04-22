from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class User(GraphObject):
    __primarykey__ = 'username'

    username = Property()
    email = Property()
    password = Property()
