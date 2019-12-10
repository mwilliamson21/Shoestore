from django.core.management.base import BaseCommand
from django_rest.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help ='choose a ShoeType and ShoeColor'

    def  handle(self, *args, **options):
         ShoeType.objects.create(style='Sneaker')
         ShoeType.objects.create(style='Boot')
         ShoeType.objects.create(style='Sandal')
         ShoeType.objects.create(style='Dress')
         ShoeType.objects.create(style='Other')
         ShoeColor.objects.create(color_name='Red')
         ShoeColor.objects.create(color_name='Orange')
         ShoeColor.objects.create(color_name='Yellow')
         ShoeColor.objects.create(color_name='Green')
         ShoeColor.objects.create(color_name='Blue')
         ShoeColor.objects.create(color_name='Indigo')
         ShoeColor.objects.create(color_name='Violet')
         ShoeColor.objects.create(color_name='White')
         ShoeColor.objects.create(color_name='Black')
         
         