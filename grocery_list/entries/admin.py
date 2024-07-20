from django.contrib import admin
from .models import GroceryEntry
# Register your models here.
class GroceryEntryAdmin(admin.ModelAdmin):
    ...

admin.site.register(GroceryEntry, GroceryEntryAdmin)
