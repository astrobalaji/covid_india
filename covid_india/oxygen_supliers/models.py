from django.db import models

# Create your models here.
class oxy_sup(models.Model):
    state_code = models.CharField(max_length = 20)
    State = models.CharField(max_length = 2000)
    City = models.CharField(max_length = 2000)
    Contact = models.CharField(max_length = 2000)
    Number = models.CharField(max_length = 20000)
