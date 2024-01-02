from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    quanity = models.IntegerField(default=0)
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    


