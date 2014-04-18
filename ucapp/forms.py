__author__ = 'ericxiao'
###from models import UserProfile
from django import forms
from django.contrib.auth.models import User
from registration_email.forms import generate_username
attrs_dict={'class':'form-control'}

class NewEmailRegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs_dict))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label="Password (repeat)")

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return email.lower()
        raise forms.ValidationError('Someone has already been registered with that email.')

    def clean(self):
        data = self.cleaned_data
        if not 'email' in data:
            return data
        if ('password1' in data and 'password2' in data):
            if data['password1'] != data['password2']:
                raise forms.ValidationError( "The two password fields didn't match.")
        self.cleaned_data['username'] = generate_username(self.cleaned_data['email'])
        # Create a temporary UserProfile, to be linked to forthcoming new User instance
        profile, created = User.objects.get_or_create(email=self.cleaned_data['email'])
        profile.name = self.cleaned_data['name']
        profile.save()
        return self.cleaned_data