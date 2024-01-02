from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
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
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
  
  
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete =  models.CASCADE)
    quantity = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.id
    
class Order(models.Model):
    PENDING_CHOICE = 'P'
    CONFIRM_CHOICE = 'CF'
    CANCEL_CHOICE = 'C'
    COMPLETED_CHOICE = 'CP'
    STATUS_CHOICES = [
        (PENDING_CHOICE , 'P'),
        (CANCEL_CHOICE , 'C'),
        (COMPLETED_CHOICE , 'CP'),
        (CONFIRM_CHOICE, 'CF')
    ]
    
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(
        max_length = 2,
        choices = STATUS_CHOICES,
        default = PENDING_CHOICE
    )
    payment_status = models.BooleanField(default = False)
    shipping_address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.id  
    
 
class OrderItem(models.Model):
    PENDING_CHOICE = 'P'
    CONFIRM_CHOICE = 'CF'
    CANCEL_CHOICE = 'C'
    COMPLETED_CHOICE = 'CP'
    STATUS_CHOICES = [
        (PENDING_CHOICE , 'P'),
        (CANCEL_CHOICE , 'C'),
        (COMPLETED_CHOICE , 'CP'),
        (CONFIRM_CHOICE, 'CF')
    ]
    product = models.ForeignKey(Product, on_delete =  models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default = 1)
    status = models.CharField(
        max_length = 2,
        choices = STATUS_CHOICES,
        default = PENDING_CHOICE
    )    
    
    def __str__(self):
        return self.id   


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete =  models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    star = models.IntegerField(validators=[MaxValueValidator(5)])
    
    def __str__(self):
        return self.id
    

    


    

    
     
    