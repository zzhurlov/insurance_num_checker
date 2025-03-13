from django.db import models


class InsuranceNumber(models.Model):
    number = models.CharField(max_length=14)
