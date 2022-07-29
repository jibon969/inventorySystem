from django.shortcuts import render, get_object_or_404
from .models import Inventory
from .forms import InventoryForm


def index(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories,
    }
    return render(request, "inventory/inventory.html", context)


def per_product(request, pk):
    inventories = get_object_or_404(Inventory, pk=pk)
    context = {
        "inventory": inventories,
    }
    return render(request, "inventory/per_product.html", context)


def add_inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            form = InventoryForm()
        context = {
            'form': form
        }
        return render(request, "inventory/add_inventory.html", context)
