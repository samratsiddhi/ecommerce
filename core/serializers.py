from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *

# class UserSerialirez(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'password',
#             'email'
#         )
#         extra_kwargs = {'password': {'write_only': True}}
        
#     def create(self, validated_data):    
#         instance = User.objects.create_user(**validated_data)
#         return instance
        

    #     user = User.objects.create(username = validated_data['username'])
    #     user.password =  make_password(validated_data['password'])
    #     user.save()
    #     return user
    
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        return User.objects.create_user(email = email , password =password)
    
    def validate_password(self, value):
        if len(value)<8:
            raise serializers.ValidationError("password mustbe atleast 8 charecters")
        return value
    
    def validate_email(self,value):
        if User.objects.filter(email =value).exists():
            raise serializers.ValidationError({
                "email" : "email already exists"
            })
        return value
            
    def validate(self, attrs):        
        if attrs.get('confirm_password') != attrs.get('password'):
            raise serializers.ValidationError({
                "password" : "passwords do not match"
            })
        return super().validate(attrs)
        
        