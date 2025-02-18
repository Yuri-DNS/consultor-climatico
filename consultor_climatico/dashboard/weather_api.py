import requests
from .models import WeatherConfig

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_api_key():
    """Busca a API key no WeatherConfig. Se não existir, retorna None ou uma chave default."""
    try:
        config = WeatherConfig.objects.first()
        return config.api_key if config else None
    except Exception as e:
        return None


def get_weather(city_name):
    """Faz uma requisição para a API OpenWeatherMap e retorna os dados da cidade."""
    api_key = get_api_key()
    if not api_key:
        # Opcional: Você pode lançar um erro ou retornar uma resposta padrão
        raise Exception("API Key for OpenWeatherMap is not configured.")

    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",  # Celsius
        "lang": "pt"  # Português
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None