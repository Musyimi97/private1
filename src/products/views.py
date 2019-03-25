
from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request):
    context = {
        'title': obj.title,
        'description': obj.description,
    }
    return  render(request,"product/detail.html",context)
