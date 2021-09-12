from django import forms
from django.forms import forms
from .models import Contact

class AddForm(forms.Form):
 class Meta:
  model = Contact
  fields = ('name','relation','phone','email','address',)