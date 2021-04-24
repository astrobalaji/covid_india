from django.db import models

# Create your models here.
class whatsapp_groups(models.Model):
    state = models.CharField(max_length = 200)
    state_code = models.CharField(max_length = 20)
    group_url = models.CharField(max_length = 2000)
