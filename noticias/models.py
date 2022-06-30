from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    # Main
    date = models.CharField(max_length=30, blank=True, default=None)
    title = models.CharField(max_length=150, blank=True, default=None)
    category = models.CharField(max_length=30, blank=True, default=None)
    autor = models.CharField(max_length=100, blank=True, default=None)
    image = models.CharField(max_length=250, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None)
    views = models.BigIntegerField()

    # Secundary
    language = models.CharField(max_length=10, blank=True, default=None)
    history = models.CharField(max_length=30, blank=True, default=None)
    dominio = models.CharField(max_length=100, blank=True, default=None)
    link = models.CharField(max_length=250, blank=True, default=None)
    link_autor = models.CharField(max_length=250, blank=True, default=None)
    body_news = models.TextField(null=True, blank=True, default=None)