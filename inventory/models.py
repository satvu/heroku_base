from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

# Ingredients - have a name and count of it in the inventory
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

#Menu Category 
class MenuCategory(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

# Menu Items
class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        'MenuCategory',
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    

    def __str__(self):
        return self.name

# An order made by a user for food
class Order(models.Model):
    when = models.DateTimeField()
    items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.when

# Holiday, days when the Container is closed
class Holidays(models.Model):
    name = models.CharField(max_length=30)
    when = models.DateTimeField()

    def __str__(self):
        return self.name

     
