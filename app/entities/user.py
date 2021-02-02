import json

class User():
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
        
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)