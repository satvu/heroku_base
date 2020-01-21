from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

# Ingredients - have a name and count of it in the inventory
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    
# Menu Items
class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)