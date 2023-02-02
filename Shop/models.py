from django.db import models
from Ecomerce.settings import AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantite = models.IntegerField(default=1)
    description =models.TextField()
    image = models.ImageField(upload_to='images')
    
    
    def __str__(self):
        return self.name
    
    
