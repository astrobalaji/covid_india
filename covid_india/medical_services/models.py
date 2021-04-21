from django.db import models

# Create your models here.
class med_serv(models.Model):
    state = models.CharField(max_length=2000)
    state_code = models.CharField(max_length = 10)
    dist_name = models.CharField(max_length= 2000)
    address = models.CharField(max_length = 20000)
    email = models.CharField(max_length = 2000)
    telephone = models.CharField(max_length = 200)
