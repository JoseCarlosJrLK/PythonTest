from django.db import models

# Create your models here.

class Produto(models.Model):
	nome = models.CharField(max_length=100)
	preco = models.DecimalField(max_digits=7, decimal_places=2)
	descricao = models.TextField()

	def __str__(self):
		return self.nome

