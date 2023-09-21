from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Enrol(models.Model):
    #creating enrol model for enrollment form
    firstname = models.TextField(max_length = 200)
    lastname= models.TextField(max_length = 200)
    emailid  = models.EmailField()
    phoneNumber = PhoneNumberField( null = True, blank = False) # Here
    course = models.TextField()

    def __str__(self):
        return self.firstname + " "+ str(self.lastname)+ " "



class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class StudentJoin(models.Model):

    name = models.CharField(max_length = 20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)
    email = models.EmailField(max_length =30)
    mobile_no = models.CharField(max_length=10)
    course = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Demo(models.Model):

    coursename = models.CharField(max_length=40)
    trainername = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    coursetype = models.CharField(max_length=40)


    def __str__(self):
        return self.coursename




    


