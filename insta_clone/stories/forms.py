from django import forms 
from .models import Story 

from django.forms import ClearableFileInput


class NewStoryForm(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={}), required=True)

	class Meta:
		model = Story
		fields = ('content', 'caption')