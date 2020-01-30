from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    holidays = Holiday.objects.all()
    return render(request, "index.html", {"holidays": holidays})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def menu(request):
    menuCategories = MenuCategory.objects.all()
    menu_dictionary = dict()

    for category in menuCategories:
        menuItems = MenuItem.objects.filter(category=category)
        menu_dictionary[category.name] = list(menuItems)

    return render(request, "menu.html", {"menu_dictionary": menu_dictionary})

def active_orders(request):
    user = User.objects.get(username=request.user.username)
    if user.is_staff:
        if request.method == 'POST':
            carts = Cart.objects.filter(active = True)
            # ordered_by = 
            send_mail(
                '[The Container] Your order is ready!',
                'Please come pick up your order as soon as possible.',
                user.email,
                [],
                fail_silently=False,
            )
            return render(request, 'active_orders.html', {"carts": carts, })

        else:
            active_carts = Cart.objects.filter(active = True)
            cart_orders = dict()
            for cart in active_carts:
                cart_orders[active_carts.who_id] =  list(Order.objects.filter(cart_id = cart.id))

            return render(request, 'active_orders.html', {"carts": cart_orders})

    else:
        raise Http404("You must be a staff member to access this page")

