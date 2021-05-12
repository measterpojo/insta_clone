from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	body = forms.CharField()


	class Meta:

		model = Comment
		fields = ('body',)
