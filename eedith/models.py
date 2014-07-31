from django.db import models

# Create your models here.

class Session(models.Model):
	description = models.CharField(max_length=200)
	start_date = models.DateTimeField('date started')
	end_date = models.DateTimeField('date ended')
