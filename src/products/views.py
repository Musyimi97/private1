from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home_view(*args,**kargs):
    return HttpResponse("<h1>jumboShop</h1>")
