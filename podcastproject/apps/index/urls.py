"""
[summary]

[description: Aqui se colocan las urls propias de la aplicacion index]
"""  

# Django
from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='IndexView'),
]
