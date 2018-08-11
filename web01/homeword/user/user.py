from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return """

     Mưa, mình chưa từng ghét mà ngược lại . 
    Nhưng dạo này nó cứ mang đến nỗi sợ cho mình mỗi đêm ,
    nó làm mình mất ngủ, nó làm mình suy nghĩ ... 
    Tiên sư cha chúng nó, mất điện éo làm được bài tập ! :-@
             """

@app.route('/user/<username>')
def get_info_user(username):
    users ={
    
        'quan': {
            'name': 'Nguyễn Anh Quân',
            'age': 16,
            'gender': 'Nữ'
            },

        'tuananh': {
            'name': 'Huỳnh Tuấn Anh',
            'age': 23,
            'gender': 'Nữ'
            },

        'huyen': {
            'name': 'Hoàng Thanh Huyền',
            'age': 15,
            'gender': 'Nữ'
            },

        'lien': {
            'name': 'Phẫn Kim Liên ',
            'age': 18,
            'gender': 'Nữ'
            },

        'ngocanh': {
            'name': 'Nguyễn Ngọc Anh',
            'age': 23,
            'gender': 'Nữ'
            },

        'nhung': {
            'name': 'Nguyễn Hồng Nhung',
            'age': 21,
            'gender': 'Nữ'

            },

        'linh': {
            'name': 'Việt Linh',
            'age': 19,
            'gender': 'Nam'

            },

        'ha': {
            'name': 'Anh Hà',
            'age': 21,
            'gender': 'Nam'

            },

        'thu': {
            'name': 'Bạn Thu',
            'age': 18,
            'gender': 'Nữ'

            },

        'dieu': {
            'name': 'Bạn Diệu',
            'age': 21,
            'gender': 'Nữ'

            },

        'phuong': {
            'name': 'Chị Phương',
            'age': 21,
            'gender': 'Nữ'

            },

        'hoang': {
            'name': 'Anh Hoàng',
            'age': 21,
            'gender': 'Nam'

            }
        }
    if username not in users:
        return("Error: User not found !!!")
    else:
        return render_template("index.html", users= users, username= username)
    

if __name__ == '__main__':
  app.run(debug=True)
 