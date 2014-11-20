from django import forms
from models import Internship, Contact
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
 
class InternshipForm(forms.ModelForm):

	class Meta:
		model = Internship;
		fields = ('intern_role', 'employer', 'email', 'description', );

 
class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact;
		fields = ('email', 'subject', 'message');