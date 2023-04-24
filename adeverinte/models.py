from django.db import models

# Create your models here.
class Adeverinta(models.Model):
    ASTEPTARE = 0
    ACCEPTAT = 1
    RESPINS = 2
    STARI = (
        (ASTEPTARE, "ASTEPTARE"),
        (ACCEPTAT, "ACCEPTAT"),
        (RESPINS, "RESPINS"),
    )
    subsemnatul = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    motivatie = models.CharField(max_length=1000)
    numar_de_inregistrare_comun = models.IntegerField()
    nr = models.IntegerField()
    specilizare = models.ManyToManyField('specializari.Specializari')
    data = models.DateField()
    acord_decan = models.BooleanField()
    decan = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='decan')
    acord_secretar = models.BooleanField()
    secretar = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='secretar')
    acord_secretar_sef = models.BooleanField()
    secretar_sef = models.ForeignKey('users.Users', on_delete=models.CASCADE, related_name='secretar_sef')
    stare = models.IntegerField(choices=STARI, default=ASTEPTARE)

