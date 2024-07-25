from django.shortcuts import render
from .models import GroceryEntry
# Create your views here.


def get_all_grocery_entries(request):
    if request.method == 'POST':
        obj = GroceryEntry()
        obj.name = request.POST.get('name')
        obj.quantity = request.POST.get('quantity')
        if obj.quantity == "":
            obj.quantity = None
        obj.importance_color = request.POST.get('importance_color')
        obj.unit = request.POST.get('unit')
        obj.brand = request.POST.get('brand')
        obj.store = request.POST.get('store')
        obj.save()

    list_data = GroceryEntry.objects.all()
    amount = GroceryEntry.objects.count()
    context = {
        'groceries_list': list_data,
        'amount_in_list': amount
    }
    return render(request, 'entries/list.html', context)

def get_single_entry(request, entry_id):
    entry = GroceryEntry.objects.all()[entry_id - 1]
    name = entry.name or None
    quantity = entry.quantity or None
    importance_color = entry.importance_color or None
    unit = entry.unit or None
    brand = entry.brand or None
    store = entry.brand or None
    context = {
        'entry_id': entry_id,
        'entry': entry,
        'name': name,
        'quantity': quantity,
        'importance_color': importance_color,
        'unit': unit,
        'brand': brand,
        'store': store
    }
    return render(request, 'entries/entry.html', context)

