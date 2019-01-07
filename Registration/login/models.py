from django.db import models

# Create your models here.
class Registers(models.Model):
	name = models.CharField(max_length=20)
	class1 = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=20)
	subject = models.CharField(max_length=20)
	gender = models.CharField(max_length=20)
	address = models.CharField(max_length=20)

	def __str__(self):
		return self.name