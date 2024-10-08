"""
URL configuration for grocery_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import get_all_grocery_entries, get_single_entry, get_single_store, get_all_stores
urlpatterns = [
    path('', get_all_grocery_entries, name='get-all-grocery-entries'),
    path("<int:entry_id>/", get_single_entry, name='get-single-entry'),
    path('stores', get_all_stores, name='get-all-stores'),
    path("<int:store_id>", get_single_store, name='get-single-store')
]
