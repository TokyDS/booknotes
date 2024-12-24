from django import forms
from api.models import *

class BookAdd(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
        
class ConspectAdd(forms.ModelForm):
    class Meta:
        model = Conspect
        fields = '__all__'