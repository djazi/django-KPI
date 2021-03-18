from django.contrib import admin
from . models import production, production_NC, KPI
# Register your models here.
admin.site.register(production)
admin.site.register(production_NC)
admin.site.register(KPI)

