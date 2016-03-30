# -*- coding: utf-8 -*-
from django import forms
from mercadoria.cadastro.models import Mercadoria

class MercadoriaForm(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = 'codigo_mercadoria', 'tipo_mercadoria', 'nome_mercadoria', 
        'quantidade_mercadoria', 'preco_mercadoria', 'tipo_negocio'