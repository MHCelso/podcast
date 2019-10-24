"""
[summary]

[description]
"""

# Django 
from django.shortcuts import render
from django.views.generic import TemplateView

# Crea tus vistas aqui.
class IndexView(TemplateView):
	"""
	[summary]
	
	[description]
	
	Extends:
		TemplateView
	""" 
	# aqui el nombre del template este se encuentra a nivel aplicacion
	template_name = 'index.html' 
