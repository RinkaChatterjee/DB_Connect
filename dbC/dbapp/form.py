from django import forms
from .models import *

class Emp_form(forms.ModelForm):
    fname = forms.CharField(widget=forms.TextInput(),required=True,max_length=45)  # Field name made lowercase.
    id = forms.IntegerField(widget=forms.NumberInput(),required=True)  # Field name made lowercase.
    lname = forms.CharField(widget=forms.TextInput(),required=True,max_length=45)  # Field name made lowercase.
    age = forms.IntegerField(widget=forms.NumberInput(),required=False)  # Field name made lowercase.

    class Meta():
        model = Emp
        fields = ['fname','id','lname','age']