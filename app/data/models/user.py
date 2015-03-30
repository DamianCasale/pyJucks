from mongoengine import *
from bson.objectid import ObjectId
import datetime
connect('db0')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    is_active = BooleanField(default=False)
    created = DateTimeField(default=datetime.datetime.now)
    
    @staticmethod
    def isValidUsername(username):
        try:
        	User.objects(email=username).get()
        	return True
        except:
        	return False

    @staticmethod
    def getUserData(id):
        print "id %s"%id
        return User.objects(id=ObjectId(id)).get().to_json()

    @staticmethod
    def getUserLogin(username,password):
        print "username %s"%username
        return User.objects(email=username).get().to_json()