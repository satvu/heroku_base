from django.db import models
from accounts.models import CustomUser

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
        'CategoriasDelMenu',
        on_delete=models.DO_NOTHING,
    )
    price = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    ingredients = models.ManyToManyField(Ingrediente)
    

    def __str__(self):
        return self.name

# Cart holding orders, associated with a user
class Cart(models.Model):
    who_id = models.ForeignKey(
        'accounts.CustomUser',
        on_delete = models.CASCADE
    )
    when = models.DateTimeField(auto_now_add = True)
    order_total =  models.DecimalField(decimal_places = 2, max_digits = 6, default = 0.0)
    active = models.BooleanField(default = False)


    def save(self, *args, **kwargs):
        if not self.id:
            super(Cart, self).save(*args, **kwargs)
        else:
            total = 0.0 # should be DecimalField not integer or float for prices
            for item in Orden.objects.filter(cart_id=self.id):
                total += (item.quantity * item.item_id.price)

            self.order_total = total # again this should be changed to DecimalField
            super(Cart, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.who_id) + ' cart'


# An order made by a user for food
# It has one MenuItem, the number of those items being ordered, 
# when it was ordered, and the cart it belongs to
class Orden(models.Model):
    item_id = models.ForeignKey(
        'ElementosDelMenu', 
        on_delete = models.DO_NOTHING,
        default=1
        )
    quantity = models.IntegerField(default = 0)
    cart_id = models.ForeignKey(
            'Cart', 
            on_delete = models.DO_NOTHING,
            default=1
        )

    def __str__(self):
        return self.item_id.name
        
# Holiday, days when the Container is closed
class DiasLibre(models.Model):
    name = models.CharField(max_length=30)
    when = models.DateField()

    def __str__(self):
        return self.name

     
