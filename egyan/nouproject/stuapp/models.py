from django.db import models

# Create your models here.
class Response(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=50)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    responsetype=models.CharField(max_length=100)
    responsetext=models.CharField(max_length=5000)