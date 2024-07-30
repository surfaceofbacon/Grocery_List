from django.shortcuts import render
from .models import GroceryEntry, Store
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
        obj.store_id = request.POST.get('store') or None
        obj.save()
    stores_data = Store.objects.all()
    list_data = GroceryEntry.objects.all()
    amount = GroceryEntry.objects.count()
    context = {
        'groceries_list': list_data,
        'amount_in_list': amount,
        'stores': stores_data
    }
    return render(request, 'entries/list.html', context)

def get_single_entry(request, entry_id):
    entry = GroceryEntry.objects.all()[entry_id - 1]
    name = entry.name or None
    quantity = entry.quantity or None
    importance_color = entry.importance_color or None
    color_code = GroceryEntry.importance_color_choices.get(importance_color)
    unit = entry.unit or None
    brand = entry.brand or None
    store = entry.store or None
    context = {
        'name': name,
        'quantity': quantity,
        'importance_color': color_code,
        'unit': unit,
        'brand': brand,
        'store': store
    }
    return render(request, 'entries/entry.html', context)

