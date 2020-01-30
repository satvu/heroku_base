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
    list_display = ('when',)

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'when')

admin.site.register(DiasLibre, HolidayAdmin)
admin.site.register(Ingrediente, IngredientAdmin)
admin.site.register(CategoriasDelMenu, MenuCategoryAdmin)
admin.site.register(ElementosDelMenu, MenuItemAdmin)
admin.site.register(Orden, OrderAdmin)
