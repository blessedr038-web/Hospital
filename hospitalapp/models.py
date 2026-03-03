from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    gender = models.CharField(max_length = 10)
    age = models.IntegerField()
    dob = models.DateField()
    datetime = models.DateTimeField()
    medicalhistory = models.TextField()


    def __str__(self):
        return self.name