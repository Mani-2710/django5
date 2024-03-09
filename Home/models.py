from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def _str_(self):
        return self.username



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


