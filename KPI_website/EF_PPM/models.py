from django.db import models

# Create your models here.


class production(models.Model):
    ID_prod = models.IntegerField()
    code_article = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ID_prod} {self.code_article} {self.Date} {self.heure}"


class production_NC(models.Model):
    ID_prod_NC = models.IntegerField()
    code_article = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ID_prod_NC} {self.code_article} {self.Date} {self.heure}"

class KPI(models.Model):
    ID_per = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    heure = models.CharField(max_length=100)
    EFF_h = models.CharField(max_length=100)
    PPM_h = models.CharField(max_length=100)
    EFF_j = models.CharField(max_length=100)
    PPM_j = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ID_per} {self.Date} {self.heure} {self.EFF_h}  {self.PPM_h} {self.EFF_j} {self.PPM_j} "
