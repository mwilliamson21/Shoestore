from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=250)

    def __str__(self):
        return'{} @ {}'.format(self.name, self.url)

class ShoeType(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return'{} '.format(self.style)

class ShoeColor(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return'{}'.format(self.color_name)

class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=100)

    def __str__(self):
        return'{} @ {}'.format(self.brand_name, self.manufacturer)
    



