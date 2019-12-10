# My family raised sheep when I was a kid growing up on the African Savanna

from rest_framework import viewsets
from shoestore import models, serializers

class ManufacturerView(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer

class ShoeTypeView(viewsets.ModelViewSet):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeTypeSerializer

class ShoeColorView(viewsets.ModelViewSet):
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeColorSerializer

class ShoeView(viewsets.ModelViewSet):
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeSerializer
