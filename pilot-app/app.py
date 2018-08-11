from flask import Flask, render_template
import mlab
from models.service import Service

app = Flask(__name__)

mlab.connect()

# design database
# class Service(Document): 
#     name = StringField()  # Field : là các trường ví dụ như name yob trong document
#     yob = IntField() 
#     gender = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender= gender, yob__gte= 1998, address__exact= "Hà Nộiiiii") # lấy ra tất cả các document của collection service

    return render_template("search.html", all_service= all_service)

if __name__ == '__main__':
    app.run(debug=True)
 