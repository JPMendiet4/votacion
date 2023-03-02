import requests
from rest_framework import serializers
from election_app.models import Municipality


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ['id', 'name', 'active']
        read_only_fields = ['id']

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
        # Get the count of active municipalities
        active_count = Municipality.objects.filter(active=True).count()
        # If there are already 1122 active municipalities, raise a validation error
        if active_count >= 1122:
            raise serializers.ValidationError('No se pueden crear más de 1122 municipios')
        return {'name': municipality_name.lower()}
