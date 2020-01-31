from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from django.core.mail import send_mail
from accounts.models import *

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
    alert_flag = False
    # try:
    item = 'nada'
    if request.method == 'POST':
        item = str(request.POST.get('item'))
        number = int(request.POST.get('number'))
        # get the current cart of this person 
        cart = Cart.objects.get(who_id = request.user)

        # check if this is an order
        orders_in_cart = list(Orden.objects.filter(cart_id = cart.id))
        order_exists = False
        if len(orders_in_cart) > 0:
            # edit that order if so
            for order in orders_in_cart:
                if order.item_id.name == item:
                    order.quantity = number 
                    order.save()
                    order_exists = True

        # else create a new order for the cart 
        if not order_exists:
            order_item = ElementosDelMenu.objects.get(name = item)
            new_order = Orden(item_id = order_item, quantity = number, cart_id = cart)
            new_order.save()

        alert_flag = True
        cart.save()

    menuCategories = CategoriasDelMenu.objects.all()
    menu_dictionary = dict()

    for category in menuCategories:
        menuItems = ElementosDelMenu.objects.filter(category=category)
        menu_dictionary[category.name] = list(menuItems)

    return render(request, "menu.html", {"menu_dictionary": menu_dictionary, "alert_flag": alert_flag, "add-item": item })

    # except:
    #     raise Http404("ERROR: INVALID USER OR ACTION")

def active_orders(request):
    user = CustomUser.objects.get(username=request.user.username)
    if user.is_staff:
        if request.method == 'POST':
            # set to inactive the cart being deleted and remove orders
            username = request.POST.get('user')
            user = User.get(username = username)
            del_cart = Cart.objects.filter(who_id = user)
            del_cart.active = False 
            del_orders = list(Order.objects.filter(cart_id = cart.id))

            for order in del_orders:
                order.delete()

            del_cart.save()

            # return all the carts again
            active_carts = Cart.objects.filter(active = True).order_by('-when')
            cart_orders = dict()
            for cart in active_carts:
                cart_orders[cart.who_id] =  (list(Orden.objects.filter(cart_id = cart.id)), cart.when)

            return render(request, 'active_orders.html', {"carts": cart_orders})

        else:
            active_carts = Cart.objects.filter(active = True).order_by('-when')
            cart_orders = dict()
            for cart in active_carts:
                cart_orders[cart.who_id] =  (list(Orden.objects.filter(cart_id = cart.id)), cart.when)

            return render(request, 'active_orders.html', {"carts": cart_orders})

    else:
        raise Http404("You must be a staff member to access this page")

        menuItems: MenuItem.objects.filter( category=F( category.name))
        menu_dictionary[category.name] = list(menuItems)
        
        return render( request, "menu.html", {"menu_dictionary": menu_dictionary})
