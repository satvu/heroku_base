from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Ingredient)
class Ingredient(admin.ModelAdmin):
    pass

@admin.register(MenuItem)
class MenuItem(admin.ModelAdmin):
    pass