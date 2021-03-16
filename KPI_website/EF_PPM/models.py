from django.db import models

# Create your models here.


class production(models.Model):
    ID_prod = models.IntegerField(max_length=100)
    code_article = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.CharField(max_length=100)


class production_NC(models.Model):
    ID_prod_NC = models.IntegerField(max_length=100)
    code_article = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.CharField(max_length=100)

class KPI(models.Model):
    ID_per = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.CharField(max_length=100)
    EFF_h = models.CharField(max_length=100)
    PPM_h = models.CharField(max_length=100)
    EFF_j = models.CharField(max_length=100)
    PPM_j = models.CharField(max_length=100)
