from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': 15, 'rows': 3}))
	class Meta:
		model = Comment
		fields = [
			"content",
		]
		# widgets = {
		# 	'content': forms.Textarea(attrs={'cols': 15, 'rows': 3})
		# }