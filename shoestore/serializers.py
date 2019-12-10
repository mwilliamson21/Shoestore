from rest_framework.serializers import HyperlinkedModelSerializer
from shoestore.models import Shoe, Manufacturer, ShoeColor, ShoeType

class ManufacturerSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['url', 'id', 'name']

class ShoeTypeSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = ShoeType
        fields = ['id', 'style']

class ShoeColorSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ShoeColor
        fields = ['id',
            'color_name'
            ]

class ShoeSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Shoe
        fields = ['size',
                  'brand_name',
                  'manufacturer', 
                  'color', 
                  'material', 
                  'shoe_type', 
                  'fasten_type']

    