from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Materias(models.Model):
	"""docstring for Materias"""
	nombreMateria=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.nombreMateria

class Estudiante(models.Model):
	"""estudiantes"""
	email=models.EmailField(max_length=50)
	nombres=models.CharField(max_length=100,blank=True)
	apellidos=models.CharField(max_length=100,blank=True)
	direccion=models.CharField(max_length=200,blank=True)
	fecha_nac=models.DateField(auto_now_add=False)
	observaciones=models.TextField()
	materia=models.ForeignKey(Materias,null=True,blank=True)
	def __str__(self):
		return self.nombres+" "+self.apellidos

