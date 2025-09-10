from django import forms
from .models import Eventos, Organizadores

class EventForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['nombre', 'fecha', 'lugar']

class OrganizaForm(forms.ModelForm):
        
    class Meta:
        model = Organizadores
        fields = ['nombre','contacto']