from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    url = "https://api.quotable.io/quotes/random"

    response = requests.get(url).json()
    quote_content = response.get('content', '')

    return render(request, 'html/home.html', {'quote_content': quote_content})
