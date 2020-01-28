from django.db import models
from django.contrib.auth.models import AbstractUser

class Section(models.Model):
    SECTION = (
        ('maestro', 'maestro'),
        ('secundaria', 'estudiante de secundaria'),
        ('cch', 'estudiante de cch'))

    condition = models.CharField(choices=SECTION, max_length=30)


    
class CustomUser(AbstractUser):
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    email = models.CharField(max_length=40) 
    seccion = models.ForeignKey(
        'Section', 
        on_delete=models.CASCADE, 
    )
    creditos = models.IntegerField()

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

class Order(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.when
# Holiday, days when the Container is closed
class Holiday(models.Model):
    name = models.CharField(max_length=30)
    when = models.DateField()

    def __str__(self):
        return self.name

