from django.db import models
from datetime import datetime
from categories.models import Category

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    subheading = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%M/%D/')
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title