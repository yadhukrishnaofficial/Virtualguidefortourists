from django.db import models

# Create your models here

class Tourist(models.Model):
    Name=models.CharField(max_length=50)
