__author__ = 'ericxiao'
from li_registration.models import UserProfile
from django import forms
from django.contrib.auth.models import User
from ucapp.models import AnalystReview
from registration_email.forms import generate_username
attrs_dict={'class':'form-control'}

class NewEmailRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict))
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs_dict))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False), label="Password (repeat)")

    class Meta:
        model = UserProfile
        fields = ('name', 'company', 'job_title', 'email', 'password1', 'password2')

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
        profile, created = UserProfile.objects.get_or_create(email=self.cleaned_data['email'])
        profile.company = self.cleaned_data['company']
        profile.job_title = self.cleaned_data['job_title']
        profile.name = self.cleaned_data['name']
        profile.save()
        return self.cleaned_data

class AnalystReviewForm(forms.ModelForm):

    class Meta:
        model = AnalystReview
        fields = ("content", "best_strength", "overall_rating", "is_anonymous")