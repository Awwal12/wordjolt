from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    # url = "https://api.quotable.io/quotes/random"

    # response = requests.get(url).json()
# , {'response':response }
    return render(request, 'html/home.html')

def main(request):
    return render(request, 'html/main.html')