from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cidade


class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AdicionarCidadeForm(forms.Form):
    cidade = forms.ModelChoiceField(
        queryset=Cidade.objects.all(),
        label="Escolha uma cidade",
        required=True
    )