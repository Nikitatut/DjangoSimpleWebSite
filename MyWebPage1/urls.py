from django.urls import path
from . import views


app_name = 'mywebpage1'

urlpatterns = [
    path('', views.index, name='index'),
]