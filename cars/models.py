from django.db import models
import datetime

# Create your models here.

class Car(models.Model):
    marka = models.CharField(max_length=16, null=True, blank=False)
    model = models.CharField(max_length=16, null=True, blank=False)
    nrRejestracyjny = models.CharField(max_length=10, blank=False, unique=True, default="")
    rokProdukcji = models.PositiveSmallIntegerField(default=1900)
    opis = models.TextField(blank=True, null=True, default="")
    obraz = models.ImageField(upload_to="zjdecia", null=True, blank=True)
    przegladTechniczny = models.DateField(default="2000-01-01")
    obslugaOkresowaData = models.DateField(default="2000-01-01")
    obslugaOkresowaKM = models.PositiveSmallIntegerField(default=0)
    rocznikOponZimowych = models.PositiveSmallIntegerField(default=2000)
    rocznikOponLetnich = models.PositiveSmallIntegerField(default=2000)
    rozmiarOpon = models.CharField(max_length=16, null=True, blank=True)
    przebiegPojazdu = models.PositiveBigIntegerField(default=0)



    def __str__(self):
        return f"{self.marka} {self.model} {self.nrRejestracyjny} {self.przegladTechniczny}"