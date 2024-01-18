from django.contrib import admin
from django.urls import path
from .views  import *

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('category', CategoryViewSet, basename= 'category')
router.register('product',ProductViewSet, basename= 'product')

urlpatterns = [
    # path('category',category_list, name="category_list")
    # ,path('category/<pk>',category_detail)
    # path('product',product_list)   

    # path('category',CategoryList.as_view(), name="category")
    # ,path('category/<pk>',CategoryDetail.as_view()),
    # # path('product',ProductList.as_view({}))
    # # ,path('product/<pk>',ProductDetail.as_view())
    
    
    # path('product',ProductViewSet.as_view({
    #   'get' : 'list',
    #   'post' :  'create',
    # })),
    
    # path('product/<pk>',ProductViewSet.as_view({
    #   'get' : 'retrieve',
    #   'put' :  'update',
    #   'delete' : 'destroy'
    # }))
   
]+router.urls
