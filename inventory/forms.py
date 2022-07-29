from django import forms
from . models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'name',
            'cost_per_item',
            'quantity_in_stock',
            'quantity_sold',
            'sales',
            'stock_date',
            'last_sales_date'
        ]
