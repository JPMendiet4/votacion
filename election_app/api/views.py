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
            errors.append(
                'El campo "Nombre" debe ser una cadena de caracteres.')
        elif not re.match("^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$", name):
            errors.append(
                'El campo "Nombre" solo debe contener letras y espacios.')
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def get_queryset(self):
        queryset = self.get_serializer().Meta.model.objects.filter(
            id=self.kwargs.get('pk')).first()
        return queryset

    def validate_data(self, data):
        errors = []
        name = data.get('name')
        if not isinstance(name, str):
            errors.append(
                'El campo "Nombre" debe ser una cadena de caracteres.')
        elif not re.match("^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$", name):
            errors.append(
                'El campo "Nombre" solo debe contener letras y espacios.')

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def patch(self, request, *args, **kwargs):
        municipality = self.get_queryset()
        if not municipality:
            return Response({'message': 'Municipio no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data.pop('id', None)

        data = self.validate_data(data)

        serializer = self.serializer_class(
            municipality, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        municipality = self.get_queryset()
        if not municipality:
            return Response({'message': 'Municipio no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        data = self.validate_data(request.data)

        serializer = self.serializer_class(municipality, data=data)
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
        # Validación 2: Verificar si existe un objeto con el id proporcionado
        obj = self.get_queryset().filter(id=pk).first()
        if not obj:
            return Response({'message': 'Municipio no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        # Validación 3: Verificar si existen objetos relacionados en otros modelos
        # lista de modelos relacionados
        related_models = ['PollingStations', 'Commune']
        for model_name in related_models:
            related_objects = getattr(obj, model_name.lower() + '_set').all()
            if related_objects.exists():
                return Response({'message': f'No se puede eliminar el municipio porque hay objetos relacionados en el modelo {model_name}'}, status=status.HTTP_400_BAD_REQUEST)

        # Si pasó las validaciones, se procede a eliminar el objeto
        obj.active = False
        obj.save()
        return Response({'message': 'El municipio ha sido eliminado correctamente'}, status=status.HTTP_200_OK)


"""Views for PollingStations."""


# class PollingStationsCreateAPIView(generics.CreateAPIView):
#     """Cretation view for PollingStations."""
#     serializer_class = PollingStationsSerializer
#     queryset