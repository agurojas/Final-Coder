from django.urls import path
from panel.views import ListaProductos,  MostrarProducto, CrearProducto, ActualizarProducto, EliminarProducto


urlpatterns=[
    path('', ListaProductos.as_view(), name='lista'),
    path('producto/<int:pk>', MostrarProducto.as_view()),
    path('crear/', CrearProducto.as_view()),
    path('actualizar/<int:pk>', ActualizarProducto.as_view()),
    path('eliminar/<int:pk>', EliminarProducto.as_view()),
    
]