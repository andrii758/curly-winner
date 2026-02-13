from django.db import models

class Article(models.Model):
    title = CharField(max_length=50)
    body = TextField()

