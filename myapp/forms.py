from django import forms
from .models import *

class CovidForm(forms.ModelForm):
    class Meta:
        model = Covid
        fields = "__all__"