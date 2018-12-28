from django.db import models

# Create your models here.

class experiments(models.Model):
    gene        = models.CharField(max_length=50)
    specie      = models.CharField(max_length=50)
    accession   = models.CharField(max_length=50)
    comparison  = models.CharField(max_length=50)
    foldchange  = models.CharField(max_length=50)
    p_value     = models.CharField(max_length=50)
    t_statistic = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.gene} {self.accession}"
