from rest_framework import viewsets, filters
from .models import Building
from .serializers import BuildingSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'owner', 'tax_paid']
    search_fields = ['ptin', 'owner']
    ordering_fields = ['tax_paid', 'tax_due']