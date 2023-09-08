from django.urls import path
from .views import home, main

urlpatterns = [
    path('', home, name='home'),
    path('main/', main, name='main'),
    # path('render_template/', render_template_view, name='render_template'),
]
