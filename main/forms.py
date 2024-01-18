from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Your name"
        })
        self.fields['email'].widget.attrs.update({
            'class': "form-control",
            'placeholder': "Your email"
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Your subject"
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Your message",
            'rows': 7,
            'cols': 30
        })