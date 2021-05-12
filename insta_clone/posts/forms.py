from django import forms
from .models import Post

from django.forms import ClearableFileInput

class NewPostForm(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'cols': '100'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

	class Meta:
		model = Post
		fields = ('content', 'caption', 'tags')