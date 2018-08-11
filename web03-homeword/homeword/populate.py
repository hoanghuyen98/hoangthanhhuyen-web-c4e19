from models.service import Service, Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
for i in range(50):
    print("Saving service", i+1,"......")
    new_service = Service(
        name = fake.name(),
        yob = randint(1990, 2000),
        gender = randint(0,1),
        height = randint(150, 190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = randint(0,1),
        description = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
        measurements = [randint(60, 100), randint(60, 100), randint(60, 100)],
        image = 'https://dantricdn.com/thumb_w/640/2017/hotgirl-reuters-kieu-trinh6-1496928968014.jpg'
    )
    new_service.save()

# for i in range(50):
#     print("Saving customer", i+1,"......")
#     new_customer = Customer(
#         name = fake.name(),
#         gender = randint(0,1),
#         email = fake.email(),
#         phone = fake.phone_number(),
#         job = fake.job(),
#         company = fake.company(),
#         contacted = choice([True, False])
       
#     )    
#     new_customer.save()

    