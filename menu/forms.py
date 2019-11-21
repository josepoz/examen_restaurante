from django import forms
from .models import Menu, Plato

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('nombre', 'cocinero_responsable', 'platos', 'costo_total')

    def __init__ (self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields["platos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["platos"].help_text = "Ingrese los platos que participaron que el CLiente desea"
        self.fields["platos"].queryset = Plato.objects.all()