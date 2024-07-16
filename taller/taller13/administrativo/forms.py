from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre por favor'),
            'direccion': _('Ingrese la direccion por favor'),
            'ciudad': _('Ingrese su ciudad por favor'),
            'tipo': _('Ingrese el tipo por favor'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if valor.startswith('L'):
            raise forms.ValidationError("EL nombre de la ciudad no puede comenzar con L mayuscula")
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costo', 'numero_cuartos',  'edificio']
        labels = {
            'nombrePropietario': _('Ingrese el nombre del propietario por favor'),
            'costo': _('Ingrese el costo por favor'),
            'numero_cuartos': _('Ingrese el numero de cuartos por favor'),
            'edificio': _('Ingrese al Departamento que pertenece por favor'),
        }

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El Costo de un departamento no puede ser mayor a $100 mil.")
        return valor

    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']
        if valor == 0 or valor > 7:
            raise forms.ValidationError("El Número de cuartos no puede ser 0, ni mayor a 7")
        return valor

    def clean_nombrePropietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("El nombre completo de un propietario **no** debe tener menos de 3 palabras.")
        return valor


class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costo', 'numero_cuartos',  'edificio']

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El Costo de un departamento no puede ser mayor a $100 mil.")
        return valor

    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']
        if valor == 0 or valor > 7:
            raise forms.ValidationError("El Número de cuartos no puede ser 0, ni mayor a 7")
        return valor

    def clean_nombrePropietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("El nombre completo de un propietario **no** debe tener menos de 3 palabras.")
        return valor