from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('when',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
