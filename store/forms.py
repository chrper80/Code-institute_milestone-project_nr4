from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, required=True, label="Your name",
                           widget=forms.TextInput(attrs={'name': 'name'}))
    email = forms.EmailField(required=True, label="Your email",
                             widget=forms.TextInput(attrs={'name': 'email'}))
    message = forms.CharField(
        max_length=400, required=True, label="Your message", widget=forms.Textarea(attrs={'name': 'message'}))
