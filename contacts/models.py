from django.db import models
from datetime import datetime

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	message = models.TextField(blank=True)
	def __str__(self):
		return self.name