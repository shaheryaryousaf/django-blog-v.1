from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
