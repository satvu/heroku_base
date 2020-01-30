from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, EditProfileForm
from inventory.models import Cart, Orden
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

def edit_profile(request):
    if request.method == 'POST':
        try:
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('view_profile'))
        except: 
            raise Http404

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

def view_cart(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        cart = Cart.objects.get(who_id = user)
        
        if user.creditos != None and user.creditos > cart.order_total:
            cart.active = True 
            cart.save()

            active_carts = Cart.objects.filter(active = True)
            orders_ahead = len(active_carts)
            time_estimate = orders_ahead * 3

            return render(request, 'order_submitted.html', {'time_estimate': time_estimate, 'user': user,
                                                                'cart': cart,
                                                                'orders_ahead': orders_ahead})
        else:
            raise Http404("You do not have enough credits to order this. Please order in person at the Container")
    
    else:
        user = User.objects.get(username=request.user.username)
        cart = Cart.objects.get(who_id = user.id)
        orders = list(Orden.objects.filter(cart_id = cart.id))

        return render(request, 'view_cart.html', {'user': user, 'cart': cart, 'orders': orders})
