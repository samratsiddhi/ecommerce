from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name',]

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
    class Meta:
        model = Product
        fields = ['id', 'name' ,'price' ,'quantity' , 'discounted_price', 'category',]

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
        
        
    
        