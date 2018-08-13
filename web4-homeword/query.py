from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b5b1e858ce1ae2ba4e93237"

# service = Service.objectss.get(id= id_to_find) # obj
# service = Service.objects(id= id_to_find) # => []
service = Service.objects.with_id(id_to_find) # => obj
# print(service.to_mongo()) # hiện thị hết thông tin của obj

if service is not None:
    # delete
    # service.delete()
    # print("Deleted")

    # updata
    print("Before: ",service.to_mongo())
    service.update(set__name="Hiếu", set__yob= "1998")
    service.reload()
    print("after: ",service.to_mongo())
else:
    print("Not found ")