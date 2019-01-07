from django.db import models

# Create your models here.
class Login_details(models.Model):
	user=models.CharField(max_length=20)
	password=models.CharField(max_length=20)

class Form_newdetails(models.Model):
	username=models.CharField(max_length=20)
	email=models.EmailField()
	contact=models.CharField(max_length=12)
	course=models.CharField(max_length=20)

