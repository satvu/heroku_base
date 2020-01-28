from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

class Section(models.Model):
    SECTION = (
        ('maestro', 'maestro'),
        ('secundaria', 'estudiante de secundaria'),
        ('cch', 'estudiante de cch'))

    condition = models.CharField(choices=SECTION, max_length=30, default='1')
    
class CustomUser(AbstractUser):
    # usuario = models.CharField(max_length=20)
    # contraseña = models.CharField(max_length=20)
    # email = models.CharField(max_length=40) 
    seccion = models.ForeignKey(
        'Section', 
        on_delete=models.CASCADE, 
        blank = True, null = True
    )
    creditos = models.IntegerField(blank = True, null = True)