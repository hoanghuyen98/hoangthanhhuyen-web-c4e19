from models.service import Service, Customer
from mlab

mlab.connect()

all_service = Service.objects()
all_customer = Customer.objects()
