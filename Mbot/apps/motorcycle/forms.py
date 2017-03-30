from django import forms

from .models import Motorcycle

class MotorcycleForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = "__all__"


