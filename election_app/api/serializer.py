import requests
from rest_framework import serializers
from election_app.models import Municipality


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['id', 'name', 'active']
        

    def validate(self, value):
        url = 'https://www.datos.gov.co/resource/xdk5-pm3f.json'
        response = requests.get(url)
        if response.status_code != 200:
            raise serializers.ValidationError('Error al obtener datos del servidor')
        data = response.json()
        municipalities_list = [municipality['municipio'].lower() for municipality in data]
        municipality_name = value['name']
        if municipality_name.lower() not in municipalities_list:
            raise serializers.ValidationError('Este municipio no existe en Colombia')
        return {'name': municipality_name.lower()}
