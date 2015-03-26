from mongoengine import *

connect('db0')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    is_active = BooleanField(default=False)

    @staticmethod
    def isValidUsername(username):
        try:
        	User.objects(email=username).get()
        	return True
        except:
        	return False

    @staticmethod
    def getUserData(username):
        return User.objects(email=username).get().to_json()