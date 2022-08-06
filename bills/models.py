from django.db import models


class Bill(models.Model):
    client_name = models.CharField(max_length=100)
    client_org = models.CharField(max_length=500)
    number = models.IntegerField()
    sum = models.FloatField()
    date = models.DateField()
    service = models.CharField(max_length=500)

    class Meta:
        unique_together = ["client_org", "number"]
