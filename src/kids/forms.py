from base.models import Kid,Payment
from django import forms 

class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['full_name', 'handle', 'age', 'term', 'kid_class', 'parent_first_contact', 'parent_second_contact', 'kid_picture']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'handle': forms.TextInput(attrs={'placeholder': 're-enter kid name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age', 'min': 0}),
            'term': forms.Select(attrs={'class': 'custom-select'}),
            'kid_class': forms.Select(attrs={'class': 'custom-select'}),
            'parent_first_contact': forms.TextInput(attrs={'placeholder': 'Enter first contact number'}),
            'parent_second_contact': forms.TextInput(attrs={'placeholder': 'Enter second contact'}),
            'kid_picture': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['kid','payment_for','payment_type','amount','handle','paid_on','term_paid_for']

        widgets = {
            'kid': forms.Select(attrs={'class': 'custom-select'}),
            'payment_for': forms.Select(attrs={'class': 'custom-select'}),
            'payment_type': forms.Select(attrs={'class': 'custom-select'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'amount paid', 'min': 0}),
            'handle': forms.TextInput(attrs={'placeholder': 'enter kid name-date'}),
            'paid_on': forms.TextInput(attrs={'placeholder': 'date format : 2023-16-11'}),
            'term_paid_for': forms.Select(attrs={'class': 'custom-select'}),
        }