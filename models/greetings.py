from google.appengine.ext import ndb


class Greetings(ndb.Model):
    name = ndb.StringProperty(required=True)
    message = ndb.TextProperty(required=True)
    timestamp = ndb.DateTimeProperty(auto_now_add=True)