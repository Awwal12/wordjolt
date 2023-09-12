from django.urls import path
from .views import main, index

urlpatterns = [
    path('', index, name='index'),
    path('main/', main, name='main'),
    # path('render_template/', render_template_view, name='render_template'),
]
