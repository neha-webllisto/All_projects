from django.db import models


# Create your models here.
class Data(models.Model):
	Name = models.CharField(max_length=20)
	Subject = models.CharField(max_length=20)

	def __str__(self):
		return self.Name

