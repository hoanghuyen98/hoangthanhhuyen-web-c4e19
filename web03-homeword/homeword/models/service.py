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
    