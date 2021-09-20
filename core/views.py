from django.views import generic
from django.shortcuts import render
from . import models
from . import forms

def Grid(request):
    return render(request,"core/grid.html",locals())
