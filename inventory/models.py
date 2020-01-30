from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

# Ingredients - have a name and count of it in the inventory
class Ingrediente(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

#Menu Category 
class CategoriasDelMenu(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

# Menu Items
class ElementosDelMenu(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        CategoriasDelMenu,
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    ingredients = models.ManyToManyField(Ingrediente)
    

    def __str__(self):
        return self.name

# An order made by a user for food
class Orden(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(ElementosDelMenu)

    def __str__(self):
        return self.when
        
# Holiday, days when the Container is closed
class DiasLibre(models.Model):
    name = models.CharField(max_length=30)
    when = models.DateField()

    def __str__(self):
        return self.name

     
