from django.urls import path
from . import views
app_name = "EF_PPM"
urlpatterns = [
    path('',views.index,name='KPI'),
    path('table',views.table,name="table")
    
    
]
