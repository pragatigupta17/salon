from django.db import models

# Create your models here.
class Empoly(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    Specilastion=models.CharField(max_length=100)
    image=models.ImageField(upload_to = 'image/')
    password=models.CharField(max_length=50)

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    purpose=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rating = models.CharField(max_length=100)
    review= models.CharField(max_length=100)