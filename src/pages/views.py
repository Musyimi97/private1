from django.shortcuts import render
from django.http import HttpResponse, request


# Create your views here.
def home_view(request):
    print(request.user)
    return render(request,"home.html",{})


def contact_view(request,*args,**kargs):
    return  render(request, "contact.html",{})

def about_view(request,*args,**kargs):
    my_context={
        "my_text":"This is Jumbo shop",
        "my_list": [1313, 4218, 234, 'abc']


    }
    return  render(request, "about.html",my_context)



