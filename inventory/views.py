from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    holidays = DiasLibre.objects.all()
    return render(request, "index.html", {"holidays": holidays})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def menu(request):
    menuCategories = CategoriasDelMenu.objects.all()
    menu_dictionary = dict()
  
    for category in menuCategories:
        menuItems = MenuItem.objects.filter(category=category)
        menu_dictionary[category.name] = list(menuItems)

    return render(request, "menu.html", {"menu_dictionary": menu_dictionary})

def active_orders(request):
    user = User.objects.get(username=request.user.username)
    if user.is_staff:
        if request.method == 'POST':
            # set to inactive the cart being deleted and remove orders
            user = request.POST.get('user')
            del_cart = Cart.objects.filter(who_id = user)
            del_cart.active = False 
            del_orders = list(Order.objects.filter(cart_id = cart.id))

            for order in del_orders:
                order.delete()

            del_cart.save()

            # return all the carts again
            active_carts = Cart.objects.filter(active = True)
            cart_orders = dict()
            for cart in active_carts:
                cart_orders[active_carts.who_id] =  list(Order.objects.filter(cart_id = cart.id))

            return render(request, 'active_orders.html', {"carts": cart_orders})

        else:
            active_carts = Cart.objects.filter(active = True)
            cart_orders = dict()
            for cart in active_carts:
                cart_orders[active_carts.who_id] =  list(Order.objects.filter(cart_id = cart.id))

            return render(request, 'active_orders.html', {"carts": cart_orders})

    else:
        raise Http404("You must be a staff member to access this page")

        menuItems: MenuItem.objects.filter( category=F( category.name))
        menu_dictionary[category.name] = list(menuItems)
        
        return render( request, "menu.html", {"menu_dictionary": menu_dictionary})
