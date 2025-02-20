from django.urls import path
from .views import dashboard, registrar, logar, adicionar_cidade, remover_cidade
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path("adicionar_cidade/", adicionar_cidade, name="adicionar_cidade"),
    path('remover_cidade/<int:cidade_id>/', remover_cidade, name='remover_cidade'),
    path('registrar/', registrar, name='registrar'),
    path('login/', logar, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
