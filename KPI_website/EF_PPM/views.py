from django.http.response import HttpResponse ,JsonResponse
from django.shortcuts import render
from . models import *
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, request
from django.urls import reverse
from django.db.models import Count
from datetime import datetime, timedelta
from django.core import serializers
# Create your views here.

def data(request):
    global e
    e=request.GET.get("e")
    l = production.objects.distinct("Date").all()
    
    data = serializers.serialize('json', l)
    return JsonResponse({"data": data})
    
        

def index(request):
   
    date = production.objects.distinct("Date").all()
    

   
    if request.method == 'POST' and 'snap' in request.POST:
        
        h=request.POST['heure']
        d = datetime.strptime(h,'%H:%M') - timedelta(hours=1)
        j = production.objects.filter(Date=e,heure__lte = h ,heure__gte=d.strftime('%H:%M')).count()
        i=production_NC.objects.filter(Date=e,heure__lte = h ,heure__gte=d.strftime('%H:%M')).count()
        efh = round((j/120)*100, 2)
        ppmh = round((i/j)*1000000, 2)

        return render(request, 'index.html', {"eff": efh, "ppm": ppmh, "dates": date,  "hi": d.strftime('%H:%M')})


    if request.method == 'POST' and 'save' in request.POST:
        eff = production.objects.filter(Date=e).count()
        ppm = production_NC.objects.filter(Date=e).count()
  
        effj = round((eff/120)*100, 2)
        ppmj = round((ppm/eff)*1000000, 2)
        
        h = request.POST['heure']
        d = datetime.strptime(h, '%H:%M') - timedelta(hours=1)
        j = production.objects.filter(Date=e,heure__lte = h ,heure__gte=d.strftime('%H:%M')).count()
        i=production_NC.objects.filter(Date=e,heure__lte = h ,heure__gte=d.strftime('%H:%M')).count()
        efh = round((j/120)*100, 2)
        ppmh = round((i/j)*1000000, 2)
        k = KPI(EFF_h=efh, PPM_h=ppmh, Date=e , heure=h)
        k.save()
        

       
        
            



        return render(request, 'index.html', {"eff": effj, "ppm": ppmj, "dates": date,"QT": eff,'PNC':ppm})
    


    return render(request, 'index.html', {"dates": date})



        


def table(request):
    return render(request,'table.html')
