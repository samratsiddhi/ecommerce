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
    quantity = models.IntegerField(default=0)
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name = 'products')
    
    

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
    
    first_name = models.CharField(max_length=200 , blank =True, null = True)
    middle_name = models.CharField(blank = True,max_length=200, null = True)
    last_name = models.CharField(max_length=200, blank =True, null = True)

    
    address = models.CharField(max_length=200, blank =True, null = True)
    gender = models.CharField(
        max_length = 1,
        choices = GENDER_CHOICES,
        blank =True, 
        null = True,
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
        
    def __str__(self):
        return f"{self.first_name} ({self.user.email})"
    
    
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete =  models.CASCADE)
    quantity = models.IntegerField(default = 1)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name = 'items')
    
    def __str__(self):
        return str(self.id)
    
class Order(models.Model):
    PENDING_CHOICE = 'P'
    CONFIRM_CHOICE = 'CF'
    CANCEL_CHOICE = 'C'
    COMPLETED_CHOICE = 'CP'
    STATUS_CHOICES = [
        (PENDING_CHOICE , 'PENDING'),
        (CANCEL_CHOICE , 'CANCLED'),
        (COMPLETED_CHOICE , 'COMPLETED'),
        (CONFIRM_CHOICE, 'CONFIRMED')
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
        return str(self.id)  
    

 
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
    order = models.ForeignKey(Order, on_delete=models.PROTECT) 
    
    def __str__(self):
        return str(self.id) 
    
  


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete =  models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    star = models.IntegerField(validators=[MaxValueValidator(5)])
    
    def __str__(self):
        return str(self.id)
    

    


    

    
     
    