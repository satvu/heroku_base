from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, MenuItem

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def menu(request):
    menuItems = MenuItem.objects.all()

    return render(request, "menu.html", {"menu_items": menuItems})
# Create your views here.
def index(request):
    holidays = Holidays.objects.all()
    return render(recuest, "index.html")
