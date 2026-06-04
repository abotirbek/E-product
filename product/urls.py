from django.urls import path
from product import views

urlpatterns = [
    path('',views.get_product, name = 'get-product'),
    path('create/',views.create_product, name = 'create'),
    path('read/<int:pk>/', views.read_product, name='read'),
    path('update/<int:pk>/', views.update_product, name='update'),
    path('delete/<int:pk>/', views.delete_product, name='delete'),
    path('filter/',views.get_over_500,name='over-500'),
    path('first/', views.get_first, name='first'),
    path('last/', views.get_last, name='last'),
    path('reverse/', views.get_reverse, name='reverse'),
    path('quantity/', views.count_products, name='quantity'),
    path('existence/', views.check_existence, name='existence'),
    path('none/', views.get_none, name='none'),
    path('distinct/', views.get_distinct, name='distinct'),
    path('dict/', views.get_dict, name='dict'),
    path('tuple/', views.get_tuple, name='tuple'),
    path('list/', views.get_list, name='list'),
    path('only/', views.get_only, name='only'),
    path('defer/', views.defer, name='defer'),
    path('iterator/', views.get_iterator, name='iterator'),
    path('raw/', views.get_raw, name='raw'),
]

