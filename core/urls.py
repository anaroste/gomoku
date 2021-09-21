from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("grid", views.Grid, name="grid"),
    path("ia_play", views.Ia_play, name="ia_play"),
)
