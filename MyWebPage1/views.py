from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<center><h2>Simple Django Project From Nikita Tyutikov!!</h2></center>')

