from django import forms
from firstApp.models import Categoria, Producto

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class FormBodega(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'faltante' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'vendido' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'descuento' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'descuento' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'valor_unitario' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            )
        }
        
class FormSupervisor(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'