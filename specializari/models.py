from django.db import models

# Create your models here.
class Specializari(models.Model):
    nume = models.CharField(max_length=100)
    acronim = models.CharField(max_length=10)
    is_master = models.BooleanField(default=False)
