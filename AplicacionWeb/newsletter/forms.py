from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	fullname = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	email_base, provider = email.split("@")
	# 	domain, extesion = provider.split('.')
	# 	if not domain == 'sath':
	# 		raise forms.ValidationError("Ingrese Correo SATH") 
	# 	if not "edu" in email:
	# 		raise forms.ValidationError("Ingrese .edu ERROR")
	# 	return email


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['fullname','email']
		#exclude = ['full_name']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extesion = provider.split('.')
		if not domain == 'sath':
			raise forms.ValidationError("Ingrese Correo SATH") 
		if not "edu" in email:
			raise forms.ValidationError("Ingrese .edu ERROR")
		return email

