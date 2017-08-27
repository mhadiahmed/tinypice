from django import forms
from .models import tinytest

class tinyFormTest(forms.ModelForm):
	class Meta:
		model = tinytest
		fields = ('name','email')
        
        
