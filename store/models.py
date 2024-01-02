from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

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
    

class Customer(models.Model):
    MALE_CHOICE = 'M'
    FEMALE_CHOICE = 'F'
    OTHER_CHOICE = 'O'
    
    GENDER_CHOICES = [
        (MALE_CHOICE , 'MALE'),
        (FEMALE_CHOICE, 'FEMALE'),
        (OTHER_CHOICE, 'OTHER')
    ]
    
    address = models.CharField(max_length=200)
    gender = models.CharField(
        max_length = 1,
        choices = GENDER_CHOICES
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    