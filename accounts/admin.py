from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'creditos', 'seccion']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('creditos', 'seccion',)}),
    )

class SectionAdmin(admin.ModelAdmin):
    list_display = ['condition']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Section, SectionAdmin)