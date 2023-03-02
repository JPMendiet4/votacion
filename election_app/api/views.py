from rest_framework import generics, status
from rest_framework.response import Response

from election_app.api.serializer import MunicipalitySerializer
from election_app.models import Municipality


class MunicipalityCreateAPIView(generics.CreateAPIView):
    """Creation view for municipalities."""
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # If the serializer is valid, save the object and return a success response.
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MunicipalityReadAPIView(generics.ListAPIView):
    """List view for municipalities."""
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({'status': 'No se han agregado municipios'})
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
