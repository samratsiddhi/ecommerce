from django.contrib import admin
from django.urls import path
from .views  import *

urlpatterns = [
    # path('category',category_list, name="category_list")
    # ,path('category/<pk>',category_detail)
    
      path('category',CategoryList.as_view(), name="category_list")
    ,path('category/<pk>',CategoryDetail.as_view())
]
