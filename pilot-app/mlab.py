import mongoengine

# mongodb://admin:admin123@ds155461.mlab.com:55461/muadongkhonglanh

host = "ds155461.mlab.com"
port = 55461
db_name = "muadongkhonglanh"
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