from rest_framework import serializers

from election_app.models import (
Municipality, PollingStations, Captains, Leader, Commune, Neighborhoods, VoterData, LeaderRespNeighborhoods, CaptainCommune
)

class MunicipalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipality
        fields = ('name',)
            
        

class PollingStationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollingStations
        fields = ('name', 'address')
        
    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        ret['municipality_id'] = instance.name
        return ret 
        
class CaptainsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Captains
        fields = '__all__'