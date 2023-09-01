from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    response = requests.get(
        'https://juanroldan1989-moviequotes-v1.p.rapidapi.com/api/v1/quotes').json()
    return render(request, 'html/home.html', {'response': response})
