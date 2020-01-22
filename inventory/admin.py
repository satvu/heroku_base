from django.contrib import admin
from .models import *

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuItem)