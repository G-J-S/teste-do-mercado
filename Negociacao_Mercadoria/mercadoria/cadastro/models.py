from django.db import models

# Classe para a mercadoria
class Mercadoria(models.Model):
	# Tupla com escolhas
	TYPE_DEAL_CHOICES = (
		(u'compra', u'Compra'),
		(u'venda', u'Venda'),
	)
	#Variaveis da mercadoria
	merc_id = models.AutoField(primary_key = True)
	codigo_mercadoria = models.IntegerField(unique=True)
	tipo_mercadoria = models.CharField(max_length = 40)
	nome_mercadoria = models.CharField(max_length = 40)
	quantidade_mercadoria = models.FloatField()
	preco_mercadoria = models.FloatField()
	tipo_negocio = models.CharField(max_length = 7, choices = TYPE_DEAL_CHOICES)
