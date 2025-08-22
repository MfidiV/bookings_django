from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    """
    This form handles user registration. 
    It collects first name, email, password, and confirmation password.
    It also validates that:
      1. The email is unique.
      2. The password and confirmation match.
    """

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}), 
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'email']

    def clean_email(self):
        """
        Ensure the email is not already registered.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered!")
        return email

    def clean(self):
        """
        Ensure password and confirm_password fields match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password and confirm and password != confirm:
            raise ValidationError("Passwords do not match!")
        return cleaned_data

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="Your email", max_length=254)
