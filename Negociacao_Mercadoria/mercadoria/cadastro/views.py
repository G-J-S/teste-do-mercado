from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from mercadoria.cadastro.models import Mercadoria

class IndexView(ListView):
	model = Mercadoria
	template_name = 'index.html'
	context_object = 'nome'

class CadastroView(CreateView):
	model = Mercadoria
	fields = '__all__'
	template_name = 'cadastro.html'
	success_url = reverse_lazy('cadastro')

class ListaView(ListView):
	model = Mercadoria
	template_name = 'lista.html'
	context_object = 'nome'

class MercadoriaDelete(DeleteView):
	model = Mercadoria
	success_url = reverse_lazy('lista')