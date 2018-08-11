from mongoengine import*
# design database


class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = IntField()
    image = URLField()
    description = StringField()
    measurements = ListField(IntField())

class Customer(Document):
    name = StringField()
    gender = IntField()
    email = EmailField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()

class User(Document):
    fullname = StringField()
    email = EmailField()
    username = StringField()
    password = StringField()

class Order(Document):
    service = ReferenceField(Service)
    user = ReferenceField(User)
    time = StringField()
    is_accepted = BooleanField()

class Admin(Document):
    username = StringField()
    password = StringField()