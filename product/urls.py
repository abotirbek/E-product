from django.urls import path
from .views import get_product, create_product, read_product, update_product, delete_product

urlpatterns = [
    path('',get_product, name = 'get-product'),
    path('create/',create_product, name = 'create'),
    path('read/<int:pk>/', read_product, name='read'),
    path('update/<int:pk>/', update_product, name='update'),
    path('delete/<int:pk>/', delete_product, name='delete'),
]

