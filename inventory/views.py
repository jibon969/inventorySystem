from django.shortcuts import render
from .models import Inventory
# Create your views here.


def index(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories,
    }
    return render(request, "inventory/inventory.html", context)