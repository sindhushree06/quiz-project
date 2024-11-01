from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_img', 'location', 'gender']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # You can customize the fields further if needed
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['profile_img'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control'

        # Since user is a OneToOneField, you can access its fields as well
        self.fields['user'].widget = forms.HiddenInput()  # Hide the user field
