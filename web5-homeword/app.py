from flask import *
import mlab 
from mongoengine import*
from models.service import Service, Customer, User, Order,Admin
from datetime import*
from gmail import GMail, Message

app = Flask(__name__)
app.secret_key = 'a super secret key'
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login-admin', methods=["GET", "POST"])
def login_admin():
    if request.method == "GET":
        return render_template('login_admin.html')
    elif request.method == "POST":
        form = request.form
        username = form['username_admin']
        password = form['password_admin']

        if username == "admin" and password == "admin":
            session['logged_admin'] = True
            return redirect(url_for('admin'))
        else:
            return "Bạn nhập sai tên tài khoản hoặc mật khẩu."


@app.route('/logout_admin')
def log_out_admin():
    if 'logged_admin' in session:
        del session['logged_admin']
        return redirect (url_for('index'))
    else:
        return "Bạn chưa đăng nhập"

@app.route('/admin')
def admin():
    if 'logged_admin' in session:
        all_service = Service.objects()
        return render_template("admin.html", all_service= all_service)
    else:
        return redirect(url_for('login_admin'))


@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    if "logged_in" in session:
        return render_template ('detail.html', service = service)
    else:
        session['service_id'] = service_id
        return redirect(url_for('login'))

@app.route('/new-service', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new-service.html")
    elif request.method == "POST":
        form = request.form
        
        new_service = Service(
            name = form['name'],
            yob = form['yob'],
            gender = form['gender'],
            phone = form['phone'],
            height = form['height'],
            address = form['address']
        )
        
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update/<service_id>', methods=["GET", "POST"])
def update(service_id):
    service_to_modify = Service.objects.with_id(service_id)
    if service_to_modify is None:
        return "Not Found"
    if request.method == "GET":
        return render_template("update.html", service= service_to_modify)
    elif request.method == "POST":

        service_to_modify.update(set__name= request.form['name'],
        set__yob= request.form['yob'],
        set__phone= request.form['phone'],
        set__height= request.form['height'],
        set__address= request.form['address'],
        # set__status= request.form['status']
        )
        service_to_modify.reload()
        service_to_modify.save()
        return redirect(url_for('admin'))

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender= gender)
    return render_template("search.html", all_service= all_service )

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template("customer.html", all_customer= all_customer)

@app.route('/search-customer')
def search_customer():
    all_customer = Customer.objects(gender= 1, contacted= False)
    if len(all_customer) < 10 :
        all_customer = all_customer
    else:
        all_customer = all_customer[0:10]

    return render_template('customer.html', all_customer= all_customer) 

@app.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template('sign_in.html')
    elif request.method == "POST":
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']
        all_user = User.objects(username=username).first()
        if all_user == None:
            new_user = User(
                fullname=fullname,
                email=email,
                username=username,
                password=password
            )
            new_user.save()
            return "Tạo tải khoản thành công"
        else:
            return "Tên đăng nhập đã có người dùng "


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        account = User.objects(username=username, password=password).first()
        if account == None:
            return "Bạn nhập sai tên tài khoản hoặc mật khẩu."
        else:
            session['logged_in'] = str(account['id'])

            return redirect (url_for('index'))

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        del session['logged_in']
        return redirect (url_for('index'))
    else:
        return "Bạn chưa đăng nhập."

@app.route('/order/<service_id>')
def new_order(service_id):
    service = Service.objects.with_id(service_id)
    if service['status'] == 1:
        return "Người này đã có khách thuê, vui lòng chọn nhân viên khác"
    else:
        user_id = session['logged_in']
        user = User.objects.with_id(user_id)
        time ='{0:%H:%M %d/%m}'.format(datetime.now())
        is_accepted = False
        new_order = Order(service=service,
                          user=user,
                          time=time,
                          is_accepted=is_accepted)
        new_order.save()
        return 'Đã gửi yêu cầu'

@app.route('/order-page')
def show_order():
    all_order = Order.objects(is_accepted=False)
    return render_template('order.html', all_order=all_order)

@app.route('/user-page/<user_id>')
def show_user_order(user_id):
    all_user = User.objects.with_id(user_id)
    all_order = Order.objects(is_accepted=False, user=all_user['id'])
    return render_template('user_order.html', all_order=all_order, all_user=all_user)

@app.route('/del-order/<order_id>')
def del_order(order_id):
        all_order = Order.objects.with_id(order_id)
        all_order.delete()
        return redirect(url_for('show_user_order', user_id=session['logged_in']))

@app.route('/order-click/<order_id>')
def order(order_id):
        all_order = Order.objects.with_id(order_id)
        service_id = all_order.service.id
        all_services = Service.objects.with_id(service_id)
        all_order.update(set__is_accepted=True)
        all_services.update(set__status=False)
        user_mail = all_order['user']['email']
        html_content = ''' Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của "Mùa Đông Không Lạnh" '''
        gmail = GMail('huyenpt1001@gmail.com', 'Huyen123')
        msg = Message('Warm Winter', to= user_mail, html= html_content)
        gmail.send(msg)
        return redirect(url_for('show_order'))

if __name__ == '__main__':
    app.run(debug=True)