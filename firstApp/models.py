from django.db import models

# Create your models here.


class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.lastname + ', '+self.firstname


class Login(models.Model):
    username = models.CharField(max_length=10)
    passcode = models.CharField(max_length=10)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        plen = len(self.passcode)
        disppass = (plen*"*")
        thestring = ('Username:'+self.username+'Password:'+disppass)
        return thestring, self.passcode
