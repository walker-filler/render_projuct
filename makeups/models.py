from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return self.name
    