from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    return render(request, 'html/home.html')


def main(request):
    url = "https://api.quotable.io/quotes/random"

    response = requests.get(url)
    if response.status_code == 200:
            api_data = response.json()
    else:
        api_data = None

    context = {'api_data':api_data}
    return render(request, 'html/main.html', context)

