from django.db import models

# Create your models here.
class Enquiry(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.CharField(max_length=1000)
class StudentInfo(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.CharField(max_length=500)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)

class LoginInfo(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)
