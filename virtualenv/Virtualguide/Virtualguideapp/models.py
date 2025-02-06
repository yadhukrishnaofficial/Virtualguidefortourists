from django.db import models

# Create your models here

class Restaurants(models.Model):
    Name=models.CharField(max_length=50)
    Image=models.FileField(blank=True)
    Address=models.CharField(max_length=200, blank=True)

class Touristspot(models.Model):
    Name=models.CharField(max_length=50)
    Image = models.FileField(blank=True)
    Address = models.CharField(max_length=200, blank=True)



