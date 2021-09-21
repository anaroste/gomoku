from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse
from . import models
from . import forms
import json
from random import randint
from django.views.decorators.csrf import csrf_exempt

def pierre_vide_aleatoire(goban):
    good = False
    while good == False:
        i = randint(0, 18)
        j = randint(0, 18)
        if goban[i][j] == 'x':
            good = True
    return i, j

def Grid(request):
    return render(request,"core/grid.html",locals())

@csrf_exempt
def Ia_play(request):
    if request.method == "POST" and request.is_ajax():
        data = request.POST
        dico = json.loads(data['dico'])
        # dico['goban'] -> GOBAN
        # dico['black_caught'] -> Nombre de pierre noire capturé par les blancs
        # dico['white_caught'] -> Nombre de pierre blanche capturé par les noires
        # dico['last_hit'] -> Dernier coup joué, si last_hit == [-1, -1], l'ordi est le premier a jouer
        # dico['ia_color'] -> Couleur de l'ordi

        i, j = pierre_vide_aleatoire(dico['goban'])

        data = json.dumps({'i': i, 'j': j})
        return JsonResponse({"success" : True, 'data' : data}, status=200)
    return JsonResponse({"success" : False}, status=400)
