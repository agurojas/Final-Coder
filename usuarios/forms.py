from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuarios.models import UserProfile
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control',}),)
    password2 = forms.CharField(label='Repetir Password',widget=forms.PasswordInput(attrs={'class':'form-control',}),)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username':forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'id':'username'
                }
            ),
            'email':forms.EmailInput(
                attrs= {
                    'class':'form-control',
                    'id':'email'
                }
            )
        }


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Nombre de usuario')
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'profile_picture','city','adress']