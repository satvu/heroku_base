from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('active_orders', views.active_orders, name='active_orders'),
]