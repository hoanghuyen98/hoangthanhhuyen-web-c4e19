from flask import *
import mlab 
from mongoengine import*
from models.service import Service, Customer
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service= all_service)

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
    service= Service.objects.with_id(service_id)
    if service is not None:
        return render_template('detail.html', service= service)
    else:
        return "Not found"

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
            address = form['address'],
            status = form['status']
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

if __name__ == '__main__':
    app.run(debug=True)
 