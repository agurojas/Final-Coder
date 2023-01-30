from panApp.models import Producto
from panel.forms import FormProducto
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper
@superuser_required()
class ListaProductos(ListView):
    model = Producto
    template_name ='templates/panel/lista.html'
    context_object_name = 'productos'
    queryset = Producto.objects.all()

class MostrarProducto(DetailView):
    model = Producto
    template_name = 'templates/panel/producto.html'
    context_object_name = 'producto'
@superuser_required()
class ActualizarProducto(UpdateView):
    model= Producto
    form_class  = FormProducto
    success_url = reverse_lazy('panel:lista')
    template_name = 'templates/panel/form.html'

@superuser_required()
class CrearProducto(CreateView):
    model= Producto
    form_class  = FormProducto
    success_url = reverse_lazy('panel:lista')
    template_name = 'templates/panel/form.html'
@superuser_required()
class EliminarProducto(DeleteView):
    model = Producto
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('panel:lista')
    template_name = 'templates/panel/eliminar.html'
  

