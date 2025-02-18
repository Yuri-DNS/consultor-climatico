from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from .weather_api import get_weather
from .models import UserProfile
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
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)  # Evita erro se o perfil não existir

    cidades = user_profile.cidades.all()
    weather_data = []

    for cidade in cidades:
        data = get_weather(cidade.nome)
        if data:
            weather_data.append({
                "cidade": cidade.nome,
                "temperatura": data["main"]["temp"],
                "descricao": data["weather"][0]["description"].capitalize(),
                "icone": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
            })

    return render(request, "dashboard/dashboard.html", {"weather_data": weather_data})