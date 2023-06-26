from django.db import models


class Setari(models.Model):
    numeFacultate = models.CharField(max_length=1000)
    acronim = models.CharField(max_length=1000)
    numeUniversitate = models.CharField(max_length=1000)
