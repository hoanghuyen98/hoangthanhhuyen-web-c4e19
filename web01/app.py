from flask import Flask, render_template # import thư viện
app = Flask(__name__) # tạo 1 server app


@app.route('/') # đường dẫn đến trang chủ
def index(): 
    posts = [
        {
        'title': "Thơ con cóc",
        'content': "Trăng nay lên cao quá. Anh hôn lên má em ",
        'author': "Tuấn Anh",
        'gender': 1
        },
        {
        'title': "Thơ xàm",
        'content': "Buồn lắm cắn ngón tay chơi ",
        'author': "Liên",
        'gender': 0

        },
        {
        'title': "???",
        'content': "Nhớ ra đã ",
        'author': "Nam",
        'gender': 1

        },
        {
        'title': "Vội vàng",
        'content': "Tôi muốn tắt nắng đi ",
        'author': "Xuân diệu",
        'gender': 0

        }
        
    ]
    return render_template("index.html", posts= posts)

@app.route('/hello') # đi đến 1 chỗ là hello
def hello():
    return "Hello c4e 19"

@app.route('/say-hi/<name>/<age>')
def say_hi(name, age):
    return "Hi {0} you are {1} years old ".format(name, age)

@app.route('/sum/<int:numb1>/<int:numb2>')
def sums(numb1, numb2):
    return str(numb1 + numb2)

if __name__ == '__main__': # khi file này chạyy 1 cách trực tiếp thì sẽ chạy 1 cái j đấy ở bên trong
    app.run(debug=True) # app.run : khởi động server < chạy trực tiếp >
 # debug = True : cập nhật lại  những code mới nhất 

 # request parameter : sd cặp dấu <>