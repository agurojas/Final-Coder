from django.urls import path, include
from panApp.views import  shop, mostrarcat, list_products, about

urlpatterns=[
    path('', shop, name='shop'),
    path('about/', about),
    path('categoria/<int:id>', mostrarcat),
    path('list-products/', list_products),

]