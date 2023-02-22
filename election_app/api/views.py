from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

import re
from election_app.api.serializer import (
    MunicipalitySerializer, PollingStationsSerializer, CaptainsSerializer
)
from election_app.models import (
Municipality, PollingStations, Captains, Leader, Commune, Neighborhoods, VoterData, LeaderRespNeighborhoods, CaptainCommune
)


"""Views for Municipality."""

class MunicipalityCreateAPIView(generics.CreateAPIView):
    """Creation view for municipalities."""
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()

    def validate_data(self, data):
        errors = []
        name = data.get('name')
        if not name:
            errors.append('El campo "Nombre" es requerido.')
        elif not isinstance(name, str):
            errors.append('El campo "Nombre" debe ser una cadena de caracteres.')
        elif not re.match("^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$", name):
            errors.append('El campo "Nombre" solo debe contener letras y espacios.')
        if errors:
            raise serializers.ValidationError(errors)
        return data
    
    def post(self, request):
        data = request.data.copy()
        validated_data = self.validate_data(data)
        serializer = self.serializer_class(data=validated_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Municipio agregado correctamente'}, status=status.HTTP_201_CREATED)  


class MunicipalityReadAPIView(generics.ListAPIView):
    """Reading view for municipalities."""
    serializer_class = MunicipalitySerializer

    def get_queryset(self):
        queryset = Municipality.objects.filter(active=True)
        return queryset
    
    def list(self, request, *args, **kwargs):    
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({'error': 'No hay municipios para listar.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
    
class MunicipalityUpdateAPIView(generics.UpdateAPIView):
    """Update view for municipalities."""
    serializer_class = MunicipalitySerializer
    
    def get_queryset(self, pk):
        queryset = self.get_serializer().Meta.model.objects.filter(id=pk).first()
        print('++'*100,queryset)
        return queryset
    
    def patch(self, request, pk=None):
        municipality = self.get_queryset(pk)
        if not municipality:
            return Response({'message': 'Municipio no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(municipality, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, pk=None):
        municipality = self.get_queryset(pk)
        if not municipality:
            return Response({'message': 'Municipio no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(municipality, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class MunicipalityDestroyAPIView(generics.DestroyAPIView):
    """Destroy view for municipalities."""
    serializer_class = MunicipalitySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(active=True)

    def delete(self, request, pk=None):
        #obj = self.get_object()
        obj = self.get_queryset().filter(id=pk).first()
        if obj:
            obj.active = False
            obj.save()
            return Response({'message': 'El municipio hasido eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'Municipio no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

"""Views for PollingStations."""
    
class PollingStationsCreateAPIView(generics.CreateAPIView):
    """Creation view for Polling Stations."""
    serializer_class = PollingStationsSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Puesto de votación agregado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class PollingStationsReadAPIView(generics.ListAPIView):
    """Reading view for Polling Stations."""
    serializer_class = PollingStationsSerializer

    def get_queryset(self):
        queryset = PollingStations.objects.filter(active=True)
        if queryset:
            return queryset
        
        
class  PollingStationsUpdateAPIView(generics.UpdateAPIView):
    """Update view for Polling Stations."""
    serializer_class = PollingStationsSerializer
    
    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(active=True).filter(id= pk).first()
    
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            pollingstations_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(pollingstations_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Puesto de votación no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            pollingstations_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if pollingstations_serializer.is_valid():
                pollingstations_serializer.save()
                return Response(pollingstations_serializer.data, status=status.HTTP_200_OK)
            return Response(pollingstations_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollingStationsDestroyAPIView(generics.DestroyAPIView):
    """Destroy view for Polling Stations.."""
    serializer_class = PollingStationsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(active=True)

    def delete(self, request, pk=None):
        obj = self.get_queryset().filter(id=pk).first()
        if obj:
            obj.active = False
            obj.save()
            return Response({'message': 'El puesto de votación ha sido eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'Puesto de votación no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
    
"""Views for Captains."""    

class CaptainsCreateAPIView(generics.CreateAPIView):
    """Creation view for Captains."""
    serializer_class = CaptainsSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Capitan creado correctamente.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaptainsReadAPIView(generics.ListAPIView):
    """Reading view for Captains."""
    serializer_class = CaptainsSerializer
    
    def get_queryset(self):
        return Captains.objects.filter(active=True)
        
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({'error': 'No hay capitanes para listar.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    