from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, required=True, label="Your name")
    email = forms.EmailField(required=True, label="Your email")
    message = forms.CharField(
        max_length=400, required=True, label="Your message", widget=forms.Textarea)
