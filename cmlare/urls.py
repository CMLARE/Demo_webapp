from django.urls import path

from . import views

urlpatterns = [
    path(route='',view= views.index, name='index'),
    path(route='data', view=views.points, name='points'),
]