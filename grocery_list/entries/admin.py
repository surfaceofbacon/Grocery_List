from django.contrib import admin
from .models import GroceryEntry, Store
# Register your models here.
class GroceryEntryAdmin(admin.ModelAdmin):
    ...
class StoreAdmin(admin.ModelAdmin):
    ...
admin.site.register(GroceryEntry, GroceryEntryAdmin)
admin.site.register(Store, StoreAdmin)
