# importamos forms desde Django
from django import forms
from .models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['Nombre', 'Descripcion', 'Precio', 'Cantidad', 'Estado']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del producto'}),
            'Descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese la descripción del producto','rows':'4'}),
            'Precio': forms.NumberInput(attrs={'class':'form-control w-25'}),
            'Cantidad': forms.NumberInput(attrs={'class':'form-control w-25'}),
            'Estado': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

    # Utilizar un constructor para evitar mostrar el campo Estado en el formulario al momento de guardar
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aplicar lógica para no mostrar el campo Estado
        if not self.instance.ProductoId:
            self.fields.pop('Estado')

    
        
    
    