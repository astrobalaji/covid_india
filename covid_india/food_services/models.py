from django.db import models

# Create your models here.
class food_ser(models.Model):
    State = models.CharField(max_length=2000)
    City = models.CharField(max_length=2000)
    Area = models.CharField(max_length=2000)
    Name = models.CharField(max_length=2000)
    Number = models.CharField(max_length=2000)
    Hours = models.CharField(max_length=2000)
    Service = models.CharField(max_length=2000)
    Social = models.CharField(max_length=2000)
    Delivery = models.CharField(max_length=2000)
