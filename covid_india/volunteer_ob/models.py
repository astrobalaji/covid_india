from django.db import models

# Create your models here.
class VolunteerOB(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length = 200)
    state_code = models.CharField(max_length = 20)
    number = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    services_offered = models.CharField(max_length = 20000)
    plasma_donor = models.CharField(max_length = 200)
    blood_type = models.CharField(max_length = 200)
