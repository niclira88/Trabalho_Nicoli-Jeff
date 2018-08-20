from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models

class RegisterUser(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'cadastrousuario.html'

class Proposed_lawCreateView(CreateView):
	model = models.Proposed_law
	template_name = 'cadastroproposta.html'
	fields = ['title', 'description']
	success_url = reverse_lazy('votacao:success')

class Success(TemplateView):
	template_name = 'sucesso.html'

class Proposed_lawListView(ListView):
	model = models.Proposed_law
	template_name = 'listaproposta.html'

class Proposed_lawDetailView(DetailView):
	model = models.Proposed_law
	template_name = 'propostadetail.html'

class CommentCreateView(CreateView):
	model = models.Comment
	template_name = 'comentarios.html'
	success_url = reverse_lazy('votacao:comment')
	fields = ['comment']

class CommentUpdateView(UpdateView):
	model = models.Comment
	template_name = 'comentarioupdate.html'
	success_url = reverse_lazy('votacao:updatecomment')
	fields = ['comment']


		
