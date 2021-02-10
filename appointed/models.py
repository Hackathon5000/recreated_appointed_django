from django.db import models

# Create your models here.
class VaccCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    havevaccine = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Patient(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateofbirth = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    resident = models.BooleanField(default=False)
    epipenUser = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName