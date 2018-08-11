from flask import Flask, render_template
import mlab 
from models.service import Service, Customer
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

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
 