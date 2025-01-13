from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Hello, World!")
    return render(request, "layout.html")


def about(request):
    # return HttpResponse("Hello, About!")
    return render(request, "about.html")


def contact(request):
    # return HttpResponse("Hello, Contact!")
    return render(request, "contact.html")


