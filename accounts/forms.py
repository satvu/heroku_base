from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
       super(EditProfileForm, self).__init__(*args, **kwargs)
       del self.fields['password']
       
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email'
        )

