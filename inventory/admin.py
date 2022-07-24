from django.contrib import admin
from inventory.models import Inventory
# Register your models here.


class InventoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'cost_per_item', 'stock_date', 'last_sales_date']
    list_editable = ['cost_per_item']

    class Meta:
        model = Inventory


admin.site.register(Inventory, InventoryAdmin)

