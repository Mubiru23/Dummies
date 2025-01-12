from django import forms
from .models import Dummies
 

class DummiesForm(forms.ModelForm):
    class Meta:
        model = Dummies
        fields = ['category', 'status', 'title', 'image', 'price','description', ]

 


 