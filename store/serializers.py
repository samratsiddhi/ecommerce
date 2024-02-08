from rest_framework import serializers
from django.db.models import Q
from .models import *
from django.db import transaction

class CategorySerializer(serializers.ModelSerializer):
    
    # without using prefetch
    total_products = serializers.SerializerMethodField()
    
    #using prefetch
    # total_products = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ['id','name','total_products']
        
        
    # without pre fetched data
    def get_total_products(self,category:Category):
    #     without using reverse relation in models
        # return category.product_set.count()
    
    #     using reverse relation in models
        return category.products.count()
    
    
# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
    
#     def create(self, validated_data):
#         instance = Category.objects.create(**validated_data)
#         return instance
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all()
        ,source = 'category'
    )
    category = CategorySerializer(read_only = True)
    class Meta:
        model = Product
        fields = ('id', 
                  'name' ,
                  'price' ,
                  'quantity' , 
                  'discounted_price', 
                  'price_with_tax',
                  'category_id',
                  'category',)
        
    def get_price_with_tax(self, product:Product):
        return (product.discounted_price*0.13) + product.discounted_price

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     quantity = serializers.IntegerField()
#     price = serializers.IntegerField()
#     discounted_price = serializers.IntegerField()
#     category_id = serializers.IntegerField()
    
#     def create(self, validated_data):
#         instance  = Product.objects.create(**validated_data)
#         return instance
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.quantity = validated_data.get('quantity', instance.quantity)
#         instance.price = validated_data.get('price', instance.price)
#         instance.discounted_price = validated_data.get('discounted_price', instance.discounted_price)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#         instance.save()
#         return instance
        
        
class CustomerSerializer(serializers.ModelSerializer):
    user =serializers.HiddenField(default=serializers.CurrentUserDefault())
    first_name= serializers.CharField(required=True)
    middle_name= serializers.CharField(required=True) 
    last_name= serializers.CharField(required=True) 
    address= serializers.CharField(required=True) 
    gender= serializers.ChoiceField(required=True, choices = Customer.GENDER_CHOICES) 
    class Meta:
        model = Customer
        fields = '__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset = Product.objects.all(),
        source = "product"
    )
    
    product = ProductSerializer(read_only = True)
    class Meta:
        model = CartItem
        fields = ['id','product_id','quantity','product']
        
    def create(self, validated_data):
        request = self.context['request']
        cart = Cart.objects.get(customer__user = request.user)
        product = Cart.objects.filter(customer_cart = cart)
        raise Exception(product)
        validated_data.update({
            'cart':cart
        })
        return super().create(validated_data)

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields ="__all__"
    
        
class CartSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset = Customer.objects.all(),
        source = 'customer',   
        read_only= False  
    )
    
    items = CartItemSerializer(many= True)
    class Meta:
        model = Cart
        fields = "__all__"
        
        
        
class CartSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset = Customer.objects.all(),
        source = 'customer',   
        read_only= False  
    )
    
    items = CartItemSerializer(many= True)
    class Meta:
        model = Cart
        fields = "__all__"
        
        
@transaction.atomic()
class CancleOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    shipping_address = serializers.CharField(read_only = True)
    class Meta:
        model = Order
        fields = ['id','shipping_address','user']
        

@transaction.atomic()
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = ['id','shipping_address','user']
        
    def create(self, validated_data):
        customer = Customer.objects.get(user = validated_data.get('user'))
        cart = Cart.objects.get(customer = customer)
        cart_items = CartItem.objects.filter(cart = cart)
        order = Order.objects.create(
            customer = customer,
            shipping_address = validated_data.get('shipping_address'),
            status = Order.CONFIRM_CHOICE
        )
        order_item_objects = [
             OrderItem(
                product = item.product,
                price= item.product.price,
                quantity= item.quantity,
                order = order,
             )
        for item in cart_items     
        ]
        cart.delete()
        
        OrderItem.objects.bulk_create(order_item_objects)
        
        return order
    
    

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        

        
    

