from django.shortcuts import render
from simplemooc.polls.models import Produto

# Create your views here.

def home(request):
	nome = ('Teste de Variavel')
	produtos = Produto.objects.all()
	return render (request, "home.html", {'produtos': produtos})
