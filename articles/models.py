from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
