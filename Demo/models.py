from django.db import models


# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.CharField(max_length=100, verbose_name='Description')
    email = models.EmailField(max_length=50, verbose_name='Email')
    createdAt = models.DateTimeField(verbose_name='Created At', auto_now_add=True)
