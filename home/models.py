from django.db import models

# Create your models here.
class Contact(models.Model):
 name = models.CharField(max_length=200)
 relation = models.CharField(max_length=200)
 phone = models.CharField(max_length=20)
 email = models.CharField(max_length=200)
 address = models.TextField()