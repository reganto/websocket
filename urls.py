from tornado.web import url
from handlers import home

url_patterns = [
    url(r"/", home.HomeHandler, name='home'),
    url(r"/ss/", home.RCHandler, name='rc'),
]
