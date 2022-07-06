from django import forms
from pteforms.models import GramStain

class GramStainForm(forms.ModelForm):
    class Meta():
        model = GramStain
        fields = "__all__"
