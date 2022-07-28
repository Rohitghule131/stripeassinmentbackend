from django.db import models


class PaymentHistory(models.Model):
    id = models.AutoField(primary_key=True)
    api_version = models.DateField(null=False,blank=False)
    created = models.IntegerField(null=False,blank=False)

