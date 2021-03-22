from django.shortcuts import render
from . models import *
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, request
from django.urls import reverse
from django.db.models import Count
# Create your views here.
def index(request):
    t=120
    eff= production.objects.all().count()
    r=  round((eff/120)*100,2)
    return render(request, 'index.html', {
        
        #"eff": production.objects.aggregate(Count('ID_prod')),
        "eff": r

        

    })


def table(request):
    return render(request,'table.html')
