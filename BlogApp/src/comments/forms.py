# from django import forms

# class CommentForm(forms.Form):
# 	content_type = forms.CharField(widget=forms.HiddenInput)
# 	object_id = forms.IntegerField(widget=forms.HiddenInput)
# 	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':4, 'cols':15}))

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