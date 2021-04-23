from django.db import models

# Create your models here.
class hosp_dat(models.Model):
    state = models.CharField(max_length = 200)
    state_code = models.CharField(max_length = 20)
    pointer = models.CharField(max_length= 2000)

class hosp_city(models.Model):
    city = models.CharField(max_length = 2000)
    state_code = models.CharField(max_length = 20)
    pointer = models.CharField(max_length = 2000)
