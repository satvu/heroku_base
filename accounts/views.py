from django.shortcuts import render
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

@login_required
def view_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404

    return render(request, "profile.html", {"user": user})