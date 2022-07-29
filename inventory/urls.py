from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('per-product/<int:pk>/', views.per_product, name="per-product"),
    path('add-inventory/', views.add_inventory, name="add-inventory"),
]
