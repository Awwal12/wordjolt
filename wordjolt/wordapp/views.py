from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import HttpResponseServerError
# Create your views here.


def index(request):
    return render(request, 'html/index.html')


def main(request):
    url = "https://api.quotable.io/quotes/random"

    response = requests.get(url)
    if response.status_code == 200:
        api_data = response.json()
    else:
        api_data = None

    context = {'api_data': api_data}
    return render(request, 'html/main.html', context=context)


def error_404_view(request, exception):
    return HttpResponse("<h1>404 Server Error</h1>")


# def render_template_view(request):
#     api_data = ...  # Replace this with the logic to fetch your API data
#     context = {'api_data': api_data}
#     template = 'your_template.html'  # Replace with the path to your template
#     rendered_template = render(request, template, context)
#     return HttpResponse(rendered_template.content)
