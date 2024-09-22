from django.db import models

# Create your models here.
class mytable(models.Model):
    firstname=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)