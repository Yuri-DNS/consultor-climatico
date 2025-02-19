from django.urls import path
from .views import dashboard, registrar, logar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('registrar/', registrar, name='registrar'),
    path('login/', logar, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
