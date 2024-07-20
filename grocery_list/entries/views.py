from django.shortcuts import render
from entries.models import GroceryEntry
# Create your views here.


def get_all_grocery_entries(request):
    data = GroceryEntry.objects.all()
    return render(request, 'entries/list.html', context={'groceries_list':data})
