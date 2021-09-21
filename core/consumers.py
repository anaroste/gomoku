from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json

from random import randint
from time import sleep

def pierre_vide_aleatoire(goban):
    good = False
    while good == False:
        i = randint(0, 18)
        j = randint(0, 18)
        if goban[i][j] == 'x':
            good = True
    return i, j

class coreConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        dico = json.loads(text_data)
        # dico['goban'] -> GOBAN
        # dico['black_caught'] -> Nombre de pierre noire capturé par les blancs
        # dico['white_caught'] -> Nombre de pierre blanche capturé par les noires

        i, j = pierre_vide_aleatoire(dico['goban'])
        self.send(json.dumps({'i': i, 'j': j}))


    # def disconnect(self, message):
    #     # Called when disconnected
    #     pass