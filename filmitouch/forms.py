from django import forms
from django.forms.widgets import TextInput, EmailInput, Textarea
from filmitouch.models import ContactForm1, Newsletter


class ContForm1(forms.ModelForm):
    class Meta:
        model = ContactForm1
        fields = ['name', 'email1', 'subject', 'desc']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name', 'class': 'text-box', 'type': 'text'}),
            'email1': EmailInput(attrs={'placeholder': 'Email Address', 'class': 'text-box', 'type': 'text'}),
            'subject': TextInput(attrs={'placeholder': 'Subject', 'class': 'text-box', 'type': 'text'}),
            'desc': Textarea(
                attrs={'rows': 3, 'placeholder': 'What you want to tell us?', 'class': 'text-area text-box'})
        }


class JoinForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['Email']

        widgets = {
            'Email': EmailInput(attrs={'placeholder': 'Email Address', type: 'text'})
        }


def clean_email(self, args, **kwargs):
    email = self.cleaned_data.get("email")
    qs = Newsletter.objects.filter(email__iexact=email)
    if qs.exists():
        raise forms.ValidationError("This Email Already Exists!")
    return email
