from django.urls import path

from election_app.api.views import (
    MunicipalityCreateAPIView, MunicipalityReadAPIView, MunicipalityUpdateAPIView, MunicipalityDestroyAPIView,
    
)

urlpatterns = [
    path('municipio-crear/', MunicipalityCreateAPIView.as_view(), name='municipio-creacion'),
    path('municipio-listar/', MunicipalityReadAPIView.as_view(), name='municipio-votación'),
    path('municipio-actualizar/<int:pk>/', MunicipalityUpdateAPIView.as_view(), name='municipio-votación'),
    path('municipio-eliminar/<int:pk>/', MunicipalityDestroyAPIView.as_view(), name='municipio-votación'),
    
    # path('puesto-crear/', PollingStationsCreateAPIView.as_view(), name='municipio-creacion'),
    # path('puesto-listar/', PollingStationsReadAPIView.as_view(), name='municipio-votación'),
    # path('puesto-actualizar/<int:pk>/', PollingStationsUpdateAPIView.as_view(), name='municipio-votación'),
    # path('puesto-eliminar/<int:pk>/', PollingStationsDestroyAPIView.as_view(), name='municipio-votación'),
    
    # path('capitan-crear/', CaptainsCreateAPIView.as_view(), name='municipio-creacion'),
    # path('capitan-listar/', CaptainsReadAPIView.as_view(), name='municipio-votación'),
    # path('puesto-actualizar/<int:pk>/', PollingStationsUpdateAPIView.as_view(), name='municipio-votación'),
    # path('puesto-eliminar/<int:pk>/', PollingStationsDestroyAPIView.as_view(), name='municipio-votación'),
    
]