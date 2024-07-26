from django import forms


class OrderForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Your e-mail"})
    )
    contact_data = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your contact data"})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your address"})
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your message"})
    )