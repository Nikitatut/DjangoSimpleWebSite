from django.urls import path
from . import views


app_name = 'mywebpage2'

urlpatterns = [
    path('', views.index, name='index'),
    ]