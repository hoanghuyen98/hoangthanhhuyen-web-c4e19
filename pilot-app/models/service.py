from mongoengine import*

class Service(Document): 
    name = StringField()  # Field : là các trường ví dụ như name yob trong document
    yob = IntField() 
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()


# new_service = Service(
#     name= "Tuấn Anh",
#     yob= 1995,
#     gender= 1, # nữ
#     height= 171,
#     phone= "0911236459",
#     address= "Hoàng Mai - Hà Nội",
#     status= False
# )

# new_service.save()