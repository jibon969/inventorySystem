from django.shortcuts import render, get_object_or_404
from .models import Inventory


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