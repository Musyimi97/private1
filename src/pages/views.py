from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args,**kargs):
    return  HttpResponse("<h1>jumboShop</h1>")


def contact_view(*args,**kargs):
    return  HttpResponse("<h1>Call Us Today to shop with us</h1>")

def about_view(*args,**kargs):
    return  HttpResponse("<h1>We are an online shop selling top range shoes and clothes for men</h1>")



