from django.db import models

# Create your models here.
class Todoitem(models.Model):
    title1=models.CharField(max_length=200)