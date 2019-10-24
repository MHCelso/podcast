"""
[summary]

[description]
"""

# Django 
from django.shortcuts import render
from django.views.generic import TemplateView

# Crea tus vistas aqui.
class Index(TemplateView):
	"""
	[summary]
	
	[description]
	
	Extends:
		TemplateView
	""" 
	# aqui el nombre del template este se encuentra a nivel aplicacion
	template_name = 'index.html' 

	def index_view(request):
		"""
		[summary]
		[description: renderiza nuestro template]
		
		Arguments:
			request {[type]} -- [description]
		
		Returns:
			[type] -- [description]
		"""
		return render(template_name)