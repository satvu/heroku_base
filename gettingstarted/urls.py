from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import inventory.views
from django.contrib.auth import views as auth_views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", inventory.views.index, name="index"),
    path("db/", inventory.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("menu/", inventory.views.menu, name="menu"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('inventory/', include('inventory.urls')),
]
