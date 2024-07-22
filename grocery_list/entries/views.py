from django.shortcuts import render
from .models import GroceryEntry
# Create your views here.


def get_all_grocery_entries(request):
    data = GroceryEntry.objects.all()
    amount = GroceryEntry.objects.all().count()
    context = {
        'groceries_list': data,
        'amount_in_list': amount
    }
    return render(request, 'entries/list.html', context)



