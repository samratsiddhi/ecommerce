from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerialirez(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):    
        user = User.objects.create(username = validated_data['username'])
        user.password =  make_password(validated_data['password'])
        user.save()
        return user
        
        