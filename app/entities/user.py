import json

class User():
    def __init__(self,_id ,username=None, password=None):
        self.id = _id
        self.username = username
        self.password = password
        
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)