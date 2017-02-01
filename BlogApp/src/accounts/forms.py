from django import forms
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout
	)

User = get_user_model()

# class UserLoginForm(forms.Form):
# 	username = forms.CharField()
# 	password = forms.CharField(widget=forms.PasswordInput)

# 	def clean(self, *args, **kwargs):
# 		username = self.cleaned_data.get("username")
# 		password = self.cleaned_data.get("password")

# 		if username and password:
# 			user = authenticate(username=username, password=password)
# 			if not user:
# 				raise forms.ValidationError("This user does not exist")
# 			if not user.check_password(password):
# 				raise forms.ValidationError("Incorrect password")
# 			if not user.is_active:
# 				raise forms.ValidationError("This user is no longer active.")
# 		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserLoginForm(forms.ModelForm):
	username = forms.CharField(label='Username')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username',
			'password',
		]

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)	
			if not user:
				raise forms.ValidationError("Email or Password is incorrect.")
				#raise forms.ValidationError("This user does not exist")
			# if not user.check_password(password):
			# 	raise forms.ValidationError("Incorrect passsword")    
			# if not user.is_active:
			# 	raise forms.ValidationError("This user is not longer active.")
		return super(UserLoginForm, self).clean(*args, **kwargs)	

class UserRegisterForm(forms.ModelForm):
	email      = forms.EmailField(label='Email Address')
	password1  = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2  = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password1',
			'password2',
		]

	def clean_password(self):
		password1  = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 != password2:
			raise forms.ValidationError("Password must match")
		return password1	

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered")
		return email	
	


















