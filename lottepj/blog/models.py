from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

        
class Feedback(models.Model):
    username = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    qrcode = models.CharField(max_length=200)
    mart = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()