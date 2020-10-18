from django.db import models

# Create your models here.
class Food(models.Model):
    
    item_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to ='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

# learn passing dynamic data
class Recipies:
    name : str
    price : int
    img : str
    desc : str
    offer :bool