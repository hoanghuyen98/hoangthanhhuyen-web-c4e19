import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds133084.mlab.com:33084/warmwinter

host = "ds133084.mlab.com"
port = 33084
db_name = "warmwinter"
user_name = "admin1"
password = "admin123"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())