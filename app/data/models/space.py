from mongoengine import *
from bson.objectid import ObjectId
import datetime
connect('db0')

class Space(Document):
    name = StringField(required=True)
    users = ListField(ReferenceField('User'))
    #parent = ReferenceField('Space')
    #dir = BooleanField(default = False)
    created = DateTimeField(default=datetime.datetime.now)


    @staticmethod
    def isValidSpace(spaceId):
        try:
            Space.objects(id=spaceId).get()
            return True
        except:
            return False

    @staticmethod
    def getUserSpaces(userId):
        userId = ObjectId(userId)
        return Space.objects(users__exists=ObjectId(userId)).to_json()