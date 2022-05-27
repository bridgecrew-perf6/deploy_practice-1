from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again: ')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        ver_email = all_cleaned_data['verify_email']
        if email != ver_email:
            raise forms.ValidationError('MAKE SURE THE EMAILS MATCH!!')