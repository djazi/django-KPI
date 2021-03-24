from enum import auto
from django.db import models

# Create your models here.


class production(models.Model):
    ID_prod = models.IntegerField()
    code_article = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.TimeField()

    def __str__(self):
        return f"{self.ID_prod} {self.code_article} {self.Date} {self.heure}"


class production_NC(models.Model):
    ID_prod_NC = models.IntegerField()
    code_article = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.TimeField()


    def __str__(self):
        return f"{self.ID_prod_NC} {self.code_article} {self.Date} {self.heure}"

class KPI(models.Model):
    ID_per = models.AutoField(primary_key=True)
    Date = models.CharField(max_length=100)
    heure = models.TimeField(null=True)
    EFF_h = models.FloatField(null=True)
    PPM_h = models.FloatField(null=True)
    EFF_j = models.FloatField(null=True)
    PPM_j = models.FloatField(null=True)

    def __str__(self):
        return f"{self.ID_per} {self.Date} {self.heure} {self.EFF_h}  {self.PPM_h} {self.EFF_j} {self.PPM_j} "
