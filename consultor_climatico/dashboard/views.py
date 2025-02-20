from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from .weather_api import get_weather
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Cidade, UserProfile  # Ajuste conforme seus modelos
from django.contrib import messages

# Create your views here.

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'dashboard/registrar.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})


@login_required
def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    cidades = user_profile.cidades.all()

    weather_data = []

    for cidade in cidades:
        weather_info = get_weather(cidade.nome)
        if weather_info:
            weather_data.append({
                'cidade': cidade.nome,
                'cidade_id': cidade.id,  # Adiciona o ID da cidade
                'temperatura': weather_info['main']['temp'],
                'descricao': weather_info['weather'][0]['description'],
                'icone': weather_info['weather'][0]['icon'],
            })

    return render(request, 'dashboard/dashboard.html', {'weather_data': weather_data})


@login_required
def adicionar_cidade(request):
    if request.method == "POST":
        cidade_nome = request.POST.get("cidade_nome").strip()

        if not cidade_nome:
            messages.error(request, "O nome da cidade não pode estar vazio.")
            return redirect("dashboard")

        # Verifica se a cidade já está cadastrada
        cidade, created = Cidade.objects.get_or_create(nome=cidade_nome)

        # Obtém o perfil do usuário
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

        # Verifica se a cidade já está associada ao usuário
        if cidade in user_profile.cidades.all():
            messages.warning(request, "Você já adicionou esta cidade.")
        else:
            user_profile.cidades.add(cidade)
            messages.success(request, f"{cidade_nome} adicionada com sucesso!")

        return redirect("dashboard")

    return redirect("dashboard")  # Evita acesso direto via GET


@login_required
def remover_cidade(request, cidade_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    cidade = get_object_or_404(Cidade, id=cidade_id)

    user_profile.cidades.remove(cidade)

    return HttpResponseRedirect(reverse('dashboard'))