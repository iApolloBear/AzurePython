from django.db import models


# Create your models here.
class Promo(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    alias = models.TextField()
