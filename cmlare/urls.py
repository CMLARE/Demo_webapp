from django.urls import path

from . import views

urlpatterns = [
    path(route='',view= views.index, name='index'),
    path(route='data/xgboost', view=views.xgboost, name='xgboost'),
    path(route='test', view=views.testMap, name='test'),

]