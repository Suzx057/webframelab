from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.get_items, name='get_items'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/list/', views.item_list, name='item_list'),
]