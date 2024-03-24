from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('update/<item_id>/', views.edit_cart, name='edit_cart'),
    path('remove/<item_id>', views.remove_item_from_cart,
         name='remove_item_from_cart'),
]