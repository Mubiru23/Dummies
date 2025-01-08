from django import forms
from .models import Dummies
 

class ContentForm(forms.ModelForm):
    class Meta:
        model = Dummies
        fields = ['category', 'satus', 'title', 'image', 'price','description', ]

 


 