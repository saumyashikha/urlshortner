from django.db import models

# Create your models here.
class UrlShort(models.Model):
    original_url = models.CharField(max_length=70)
    short_url = models.CharField(max_length=70)