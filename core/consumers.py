from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json


class coreConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        pass


    def disconnect(self, message):
        # Called when disconnected
        pass