from django.contrib import admin
from .models import (
    Municipality,PollingStations, Captains, Leader, Commune, Neighborhoods, VoterData, LeaderRespNeighborhoods, CaptainCommune
)
# Register your models here.
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('active', 'id',)

admin.site.register(Municipality, MunicipalityAdmin)  

class PollingStationsAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'municipality_id', 'active')
    list_filter = ('active', 'id',)

admin.site.register(PollingStations, PollingStationsAdmin) 


class CaptainsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'phone', 'active',)
    list_filter = ('active', 'id',)  
    
admin.site.register(Captains, CaptainsAdmin)


class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'phone','captains_id', 'active',)
    list_filter = ('active', 'id',)  
    
admin.site.register(Leader, LeaderAdmin)


class CommuneAdmin(admin.ModelAdmin):
    list_display = ('name', 'municipality_id', 'active',)
    list_filter = ('active', 'id',) 
    
admin.site.register(Commune, CommuneAdmin)


class NeighborhoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'commune_id', 'active',)
    list_filter = ('active', 'id',) 
    
admin.site.register(Neighborhoods, NeighborhoodsAdmin)


class VoterDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'address', 'active',)
    list_filter = ('active', 'id',) 

admin.site.register(VoterData, VoterDataAdmin)


class LeaderRespNeighborhoodsAdmin(admin.ModelAdmin):
    list_display = ('leader_id', 'captains_id', 'active',)
    list_filter = ('active', 'id',) 
    
admin.site.register(LeaderRespNeighborhoods, LeaderRespNeighborhoodsAdmin)


class CaptainCommuneAdmin(admin.ModelAdmin):
    list_display = ('commune_id', 'captains_id', 'active',)
    list_filter = ('active', 'id',) 
    
admin.site.register(CaptainCommune, CaptainCommuneAdmin)



