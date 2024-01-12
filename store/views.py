# from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from .paginations import *


# *****using decotor *****
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

# ***** class based view   *****
# class CategoryList(APIView):
#     def get(self,request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CategorySerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'detail':'data insert successful'
#         })


# *****using mixins***** 
# class CategoryList(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
    
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.list(request , *args, **kwargs)
           
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# ***** Using generic class-based views *****
# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


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
    

# ***** class based view *****
# class CategoryDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return get_object_or_404(Category,pk=pk)
#         except Exception:
#             raise Http404
        
#     def get(self,request ,pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(
#                 serializer.data,
#                 status = status.HTTP_204_NO_CONTENT
#             )
        
#     def delete(self,request,pk):
#         category = self.get_object(pk)
#         category.delete()
#         return Response(
#             status = status.HTTP_204_NO_CONTENT
#         )
        
#     def put(self,request,pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'details' : 'successfully updated'
#             })    


# using generic view and mixins 
# class CategoryDetail(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
    
#     queryset = Category.objects.all()
#     serializer_class =  CategorySerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# using generic class view 
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset =  Category.objects.all()
#     serializer_class = CategorySerializer
    
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    @action(methods=['get'], detail=True)
    def verify(self, request, pk = None):
        return  Response("ok")
       
# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products , many = True)
#         return Response(
#            serializer.data
#         )
#     else:
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response({
#             'detail' : 'data added successfully' 
#         })

# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        
        '''
            Custum Pagination is used here
        '''
        return super().list(request, *args, **kwargs)



 