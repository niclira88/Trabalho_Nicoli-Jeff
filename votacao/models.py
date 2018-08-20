from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta

now = datetime.now()
other_time = now + timedelta(hours=1)

class Proposed_law(models.Model):
	title = models.CharField(max_length=250, verbose_name='titulo')
	description = models.TextField(verbose_name='descrição')
	resultado = models.BooleanField(default = False, verbose_name='resultado')
	final_time = models.TimeField(verbose_name='horario final', default=other_time)
	active = models.BooleanField(default=True, verbose_name='ativado')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'proposta de lei'
		verbose_name_plural = 'propostas de leis'


class Voting(models.Model):
	id_proposed = models.IntegerField(default= 0, verbose_name='id_proposed')
	id_user = models.IntegerField(default= 0, verbose_name='id_user')
	votocontra = models.IntegerField(default = 0, verbose_name='votos contra')
	votoafavor = models.IntegerField(default = 0, verbose_name='votos a favor')

	def __str__(self):
		return 'voto'

	class Meta:
		verbose_name = 'voto'
		verbose_name_plural = 'votos'

class Comment(models.Model):
	id_proposed = models.IntegerField(default= 0, verbose_name='id_proposed')
	id_user = models.IntegerField(default= 0, verbose_name='id_user')	
	comment = models.TextField(verbose_name='Comentario')

	def __str__(self):
		return self.comment

	class Meta:
		verbose_name = 'comentario'
		verbose_name_plural = 'comentarios'


