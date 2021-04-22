from django.db import models

# Create your models here.
class hosp_dat(models.Model):
    state = models.CharField(max_length = 200)
    state_code = models.CharField(max_length = 20)
    pointer = models.CharField(max_length= 2000)
