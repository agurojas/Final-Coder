from django import forms
from panApp.models import Producto

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen','categoria', 'descripcion', 'stock']
        labels = {
            'nombre':'Nombre de producto',
            'precio':'Precio',
            'imagen':'Imagen del producto',
            'categoria':'Categoria',
            'descripcion':'Descripcion',
            'stock': 'Stock',
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingresar nombre del producto',
                    'id':'nombre'
                }
            ),
            'precio':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'precio'
                }
            ),
            'imagen': forms.ClearableFileInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Subir una foto',
                    'id':'imagen'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Elige una categoria',
                    'id':'categoria'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Describe el producto',
                    'id':'descripcion'
                }
            ),
            'stock':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input',
                    'placeholder':'Diponibilidad',
                    'id':'stock'
                }
            ),
        }
