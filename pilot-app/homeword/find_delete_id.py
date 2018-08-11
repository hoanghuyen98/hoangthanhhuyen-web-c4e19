from models.service import Service
import mlab

mlab.connect()

id_to_find = '5b5da3378ce1ae2fb425c85c'

# cách 1: 
finder = Service.objects.get(id= id_to_find)
print(finder.name)

print("* "*20)
service = finder.delete()
print(finder.name," Đã xóa ")
cách 2:
finder = Service.objects.with_id(id_to_find)
if finder is not None:
    # finder.delete
    print(finder.address)   
else:
    print("Service not found")
