from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
