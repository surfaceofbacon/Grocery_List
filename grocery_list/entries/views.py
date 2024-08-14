from django.shortcuts import render
from .models import GroceryEntry, Store
# Create your views here.


def get_all_grocery_entries(request):
    if request.method == 'POST':
        form_type = request.POST.get('form-type')
        if form_type == 'check':
            entry_id = request.POST.get('entry')
            entry = GroceryEntry.objects.get(pk=entry_id)
            entry.purchased = not entry.purchased
            entry.save()
        elif form_type == 'delete':
            GroceryEntry.objects.filter(purchased=True).delete()

        elif form_type == 'entry-form':
            obj = GroceryEntry()
            obj.name = request.POST.get('entry_name')
            obj.quantity = request.POST.get('quantity')
            if obj.quantity == "":
                obj.quantity = 1
            obj.importance_color = request.POST.get('importance_color') or None
            obj.unit = request.POST.get('unit') or None
            obj.brand = request.POST.get('brand') or None
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
    entry = GroceryEntry.objects.all().filter(id=entry_id)[0]
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

def get_all_stores(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Store.objects.filter(name=name):
            Store.objects.filter(name=name).delete()
        else:
            obj = Store()
            obj.name = name
            obj.save()

    stores_data = Store.objects.all()
    amount = Store.objects.count()
    context = {
        'stores_data': stores_data,
        'amount': amount
    }

    return render(request, 'entries/stores.html', context)

def get_single_store(request, store_id):
    entry_store = Store.objects.filter(id=store_id)[0]
    name = entry_store.name or None
    items_in_store = GroceryEntry.objects.filter(store=entry_store)
    context = {
        'store': entry_store,
        'name': name,
        'items': items_in_store
    }
    return render(request, 'entries/store.html', context)