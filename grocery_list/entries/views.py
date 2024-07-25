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



