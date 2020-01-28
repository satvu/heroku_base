from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

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