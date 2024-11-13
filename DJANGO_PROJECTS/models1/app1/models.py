from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone_no=models.IntegerField()
    birth_date=models.DateField()

    def __str__(self):
        return f"{self.name,self.email}"
