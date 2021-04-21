from django.db import models

# Create your models here.
class food_ser(models.Model):
    State = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Area = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Number = models.CharField(max_length=200)
    Hours = models.CharField(max_length=200)
    Service = models.CharField(max_length=200)
    Social = models.CharField(max_length=200)
    Delivery = models.CharField(max_length=200)
