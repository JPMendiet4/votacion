from rest_framework import generics, status, serializers
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        # Save the object, passing the current user as the creator.
        serializer.save()
