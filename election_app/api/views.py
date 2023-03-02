from rest_framework import generics, status
from rest_framework.response import Response

from election_app.api.serializer import MunicipalitySerializer
from election_app.models import Municipality


class MunicipalityCreateAPIView(generics.CreateAPIView):
    """Creation view for municipalities."""
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()

    def post(self, request, *args, **kwargs):
        # POST method to create a new municipality
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MunicipalityReadAPIView(generics.ListAPIView):
    """List view for municipalities."""
    serializer_class = MunicipalitySerializer

    def get_queryset(self):
        # queryset to retrieve the list of active municipalities
        return Municipality.objects.filter(active=True)
    
    def get(self, request, *args, **kwargs):
        # GET method to retrieve the list of municipalities
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({'status': 'No se han agregado municipios'})
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MunicipalityUpdateAPIView(generics.UpdateAPIView):
    """Update view of municipalities."""
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()

    def put(self, request, *args, **kwargs):
        # PUT method to update a municipality
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        # PATCH method to partially update a municipality
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MunicipalityDestroyAPIView(generics.DestroyAPIView):
    """Delete view of municipalities."""
    serializer_class = MunicipalitySerializer
    queryset = Municipality.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


