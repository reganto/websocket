from tornado.websocket import WebSocketHandler
from handlers.base import BaseHandler

from models import User, session


class HomeHandler(BaseHandler):
    def get(self):
        self.render('auth.html')


class RCHandler(WebSocketHandler):
    def open(self):
        print("connection opened")

    def on_message(self, message):
        try:
            result = session.query(User).filter_by(username=message).first()
            assert result != None, "No record Found"
        except AssertionError as ae:
            user = User(username=message)
            session.add(user)
            self.write_message(f"Username <b>{message}</b> added to db")
        else:
            self.write_message(f"Username <b>{message}</b> already exist")
        finally:
            session.commit()

    def on_ping(self):
        print("ping")
    
    def on_pong(self, data):
        print(f"pong -> data ->{data}")
    
    def on_close(self):
        print(f"{self.close_code} - {self.close_reason}")
