from django.shortcuts import render
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, EditProfileForm
from inventory.models import Cart, Orden, ElementosDelMenu, Ingrediente
from datetime import datetime, timedelta

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
    if request.method == 'POST' and "submit_order" in request.POST:
        user = User.objects.get(username=request.user.username)
        cart = Cart.objects.get(who_id = user)

        # Check that there are enough ingredients
        submitted_orders = Orden.objects.filter(cart_id = cart.id)
        ingredients = Ingrediente.objects.all()
        # Create dictonary of all ingredients you have 
        ingredient_have_dict = dict()
        for ingredient in ingredients:
            ingredient_have_dict[ingredient.name] = ingredient.amount
        # Create dictionary of all the ingredients you need
        ingredient_need_dict = dict()
        for order in submitted_orders:
            for ing in order.item_id.ingredients.all():
                if ing.name not in ingredient_need_dict.keys():
                    ingredient_need_dict[ing.name] = 1
                else:
                    ingredient_need_dict[ing.name] += 1
        # Compare the two dictionaries
        for ingredient_needed in ingredient_need_dict.keys():
            if ingredient_need_dict[ingredient_needed] > ingredient_have_dict[ingredient_needed]:
                raise Http404("There are not enough " + ingredient_needed + " so this order cannot be processed")
        
        # Check that they have enough money
        if user.creditos != None and user.creditos > cart.order_total:
            # get the current active carts/order
            active_carts = Cart.objects.filter(active = True).order_by('when')
            orders_ahead = len(active_carts)
            # set this cart and make it active
            cart.active = True 
            user.creditos -= cart.order_total
            cart.save()
            user.save()


            # estimate using active carts
            time_estimate = 0 
            for cart in active_carts:
                time_estimate += cart.time_total
            

            return render(request, 'order_submitted.html', {'time_estimate': time_estimate, 'user': user,
                                                                'cart': cart,
                                                                'orders_ahead': orders_ahead})
        else:
            raise Http404("You do not have enough credits to order this. Please order in person at the Container")
    
    if request.method == 'POST' and "eliminar" in request.POST:
        item = str(request.POST.get('item'))
        # get the current cart of this person 
        cart = Cart.objects.get(who_id = request.user)
        order_item = ElementosDelMenu.objects.get(name = item)
        order = Orden.objects.filter(cart_id = cart.id, item_id = order_item)
        order.delete()
        cart.save()

        # to display regular page again
        user = User.objects.get(username=request.user.username)
        try:
            cart = Cart.objects.get(who_id = user.id)
            orders = list(Orden.objects.filter(cart_id = cart.id))

            return render(request, 'view_cart.html', {'user': user, 'cart': cart, 'orders': orders})

        except: 
            cart = Cart(who_id = user)
            cart.save()
            return render(request, 'view_cart.html', {'user': user, 'cart': cart})
    
    else:
        user = User.objects.get(username=request.user.username)
        try:
            cart = Cart.objects.get(who_id = user.id)
            orders = list(Orden.objects.filter(cart_id = cart.id))

            return render(request, 'view_cart.html', {'user': user, 'cart': cart, 'orders': orders})

        except: 
            cart = Cart(who_id = user)
            cart.save()
            return render(request, 'view_cart.html', {'user': user, 'cart': cart})
