from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100 ,default='SOME STRING')
    roll=models.CharField(max_length=100, default='SOME STRING')
    number=models.CharField(max_length=100 ,default='SOME STRING')
    sClass=models.CharField(max_length=100 ,default='SOME STRING')

    def __str__(self):
        return self.name