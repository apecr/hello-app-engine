import webapp2
from webapp2 import Route


app = webapp2.WSGIApplication([
    Route('/', handler='main.MainHandler'),
    Route('/greet', handler='main.GreetHandler')
], debug=True)
