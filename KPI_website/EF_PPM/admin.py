from django.contrib import admin
from . models import * #production, production_NC, KPI
# Register your models here.


class productionAdmin(admin.ModelAdmin):
    list_display = ("ID_prod", "code_article", "Date", "heure")

class production_NCAdmin(admin.ModelAdmin):
    list_display = ("ID_prod_NC", "code_article", "Date", "heure")
class KPIAdmin(admin.ModelAdmin):
    list_display = ("ID_per", "Date", "heure", "EFF_h", "PPM_h", "EFF_j", "PPM_j")
                    
                    
                   

admin.site.register(production, productionAdmin )
admin.site.register(production_NC, production_NCAdmin)
admin.site.register(KPI, KPIAdmin)

