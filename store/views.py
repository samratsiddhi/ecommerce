from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.


# class based view   
class CategoryList(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'detail':'data insert successful'
        })

# @api_view(['GET','POST'])
# def category_list(request):
    
#     if request.method == "GET":   
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'status' : 'success',
#             'message' : 'data insert successful'
#         })

# class based view
class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return get_object_or_404(Category,pk=pk)
        except Exception:
            raise Http404
        
    def get(self,request ,pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(
                serializer.data,
                status = status.HTTP_204_NO_CONTENT
            )
        
    def delete(self,request,pk):
        category = self.get_object(pk)
        category.delete()
        return Response(
            status = status.HTTP_204_NO_CONTENT
        )
        
    def put(self,request,pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'details' : 'successfully updated'
            })  

# @api_view(['GET','DELETE','PUT'])
# def category_detail(request, pk):
#     category = get_object_or_404(Category,pk=pk)
#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(
#                 serializer.data,
#                 status = status.HTTP_204_NO_CONTENT
#             )
#     if request.method == "DELETE":
#         category.delete()
#         return Response(
#             status = status.HTTP_204_NO_CONTENT
#         )
    
    # if request.method == "PUT":
    #     serializer = CategorySerializer(category, data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({
    #         'details' : 'successfully updated'
    #         })       

 