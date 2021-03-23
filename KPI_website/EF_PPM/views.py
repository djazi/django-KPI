from django.shortcuts import render
from . models import *
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, request
from django.urls import reverse
from django.db.models import Count
# Create your views here.
def index(request):

    
    
    date = production.objects.distinct("Date").all()
    eff= production.objects.all().count()
    ppm = production_NC.objects.all().count()
    pc=  round((eff/120)*100,2)
    pnc=round((ppm/eff)*1000000,2)


    return render(request, 'index.html', {
        "eff": pc,
        "ppm":pnc,
        "dates":date
    })


def table(request):
    return render(request,'table.html')
