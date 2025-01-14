from django.shortcuts import render
from django.http import HttpResponse
from .models import Pslmatches
from django.shortcuts import get_list_or_404

# Create your views here.

def home(request):
    # return HttpResponse("Hello, World!")
    psls = Pslmatches.objects.all()
    return render(request, "home.html", {'psls': psls})

def psl_details(request, psl_id):
    psl = get_list_or_404(Pslmatches, pk = psl_id)
    return render(request, "psl_details.html", {'psl':psl})


def about(request):
    # return HttpResponse("Hello, About!")
    return render(request, "about.html")


def contact(request):
    # return HttpResponse("Hello, Contact!")
    return render(request, "contact.html")


