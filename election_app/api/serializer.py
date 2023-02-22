from rest_framework import serializers

from election_app.models import (
Municipality, PollingStations, Captains, Leader, Commune, Neighborhoods, VoterData, LeaderRespNeighborhoods, CaptainCommune
)

class MunicipalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipality
        fields = '__all__'
        

class PollingStationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollingStations
        fields = '__all__'
        
class CaptainsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Captains
        fields = '__all__'