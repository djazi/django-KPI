from django.http.response import HttpResponse
from django.shortcuts import render
from . models import *
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, request
from django.urls import reverse
from django.db.models import Count
from datetime import datetime, timedelta
# Create your views here.
def index(request):

    date = production.objects.distinct("Date").all()
    eff = production.objects.all().count()
    ppm = production_NC.objects.all().count()
    pc = round((eff/120)*100, 2)
    pnc = round((ppm/eff)*1000000, 2)


    
    
    
    if request.method == 'POST' and 'snap' in request.POST:
        
        h=request.POST['heure']
        d = datetime.strptime(h,'%H:%M') - timedelta(hours=1)
        j = production.objects.filter(Date='20/03/2021',heure__lte = h ,heure__gte=d.strftime('%H:%M')).count()
        di = request.POST['datesss']

        
        return render(request, 'index.html', {"eff": pc, "ppm": pnc,"dates": date,"heu":j,"hi":d.strftime('%H:%M')})


    if request.method == 'POST' and 'save' in request.POST:
        k = KPI(EFF_h=pc, PPM_h=pnc, Date='20/03/2021', heure=request.POST['heure'])
        k.save()
        return render(request, 'index.html', {"eff": pc, "ppm": pnc, "dates": date})
    


    return render(request, 'index.html', {"dates": date})


def table(request):
    return render(request,'table.html')
