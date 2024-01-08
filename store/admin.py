from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','discounted_price','category',)
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 5


class CartItemInline(admin.TabularInline):
    model = CartItem
    autocomplete_fields = ('product',)
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer',)
    autocomplete_fields =('customer',)
    inlines = (CartItemInline,)


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    list_display = ('id',
                   'product_id',
                   'price',
                   'quantity',
                   'status',
                   'order_id'
                   )
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'status',
                    'payment_status',
                    'shipping_address',)
    inlines = (OrderItemInline,)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product','customer','star')
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'address',
                    'gender',)
    search_fields = ('first_name',)
    list_per_page = 10
    
   
