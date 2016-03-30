from django.contrib import admin
from mercadoria.cadastro.models import Mercadoria

# Classe do administrador
class MercadoriaAdmin(admin.ModelAdmin):
	list_display = ['codigo_mercadoria', 'tipo_mercadoria', 'nome_mercadoria', 
        'quantidade_mercadoria', 'preco_mercadoria', 'tipo_negocio']
	list_filter = ['tipo_negocio']											# Cria o filtro de listas
	search_fields = ['nome_mercadoria']										# Cria o campo de busca, parametro nome da mercadoria
	save_on_top = True													# Adiciona o salvar no topo do Admin
admin.site.register(Mercadoria, MercadoriaAdmin)	# Registrar no Admin