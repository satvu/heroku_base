from django.contrib import admin
from .models import *

# Register your models here.

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'quantity')

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'when')

class CartAdmin(admin.ModelAdmin):
    list_display = ('who_id', 'order_total', 'when')

admin.site.register(Cart, CartAdmin)
admin.site.register(Holiday, HolidayAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
