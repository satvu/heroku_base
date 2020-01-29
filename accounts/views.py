from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
User = get_user_model()

# TODO: use custom user signup instead once finished with the custom user
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def view_profile(request):
    try:
        user = User.objects.get(username=request.user.username)
    except:
        raise Http404

    return render(request, "profile.html", {"user": user})