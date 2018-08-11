import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds115762.mlab.com:15762/ted

host = "ds115762.mlab.com"
port = 15762
db_name = "ted"
user_name = "admin"
password = "admin123"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())