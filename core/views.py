from django.contrib.auth import authenticate,get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from .serializers import UserSerialirez



# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username,password=password)
    
    if user:
        token,_=Token.objects.get_or_create(user=user)
        
        return Response({
            'user':user.get_username(),
            'token' : token.key
        })
    
    return Response("invalid")

@api_view(['POST'])
def register(request):

    username = request.data.get('username')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')
    
    
    User = get_user_model()
    
    if User.objects.filter(username=username).exists():
        return Response(f"User already exists")

    if password == confirm_password:
        
        # user = User(username=username)
        # # user.set_password(password)
        # user.password = make_password(password)
        
        # user.save()
        
        serailzer = UserSerialirez(data = request.data)
        serailzer.is_valid(raise_exception= True)
        serailzer.save()

        
        return Response({
            'detail' : 'user register success'
        })
    return Response('Password does not match')
