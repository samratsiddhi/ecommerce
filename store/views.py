from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def category_list(request):
    
    if request.method == "GET":   
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    else:
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status' : 'success',
            'message' : 'data insert successful'
        })


@api_view(['GET','DELETE','PUT'])
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(
                serializer.data,
                status = status.HTTP_204_NO_CONTENT
            )
    if request.method == "DELETE":
        category.delete()
        return Response(
            status = status.HTTP_204_NO_CONTENT
        )
    
    if request.method == "PUT":
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'details' : 'successfully updated'
            })       

 