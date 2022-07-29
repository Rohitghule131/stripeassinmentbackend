from django.db import models

# created Customer payment History Model to Store 

class PaymentHistory(models.Model):
    name = models.CharField(verbose_name="Customer Name",max_length=50)
    email = models.EmailField(verbose_name="Customer Email")
    amount = models.FloatField(verbose_name="Total Amount")
    city = models.CharField(verbose_name="Customer Address",max_length=100)
    state = models.CharField(verbose_name="Customer Address",max_length=100)
    country = models.CharField(verbose_name="Customer Address",max_length=100)
    status = models.CharField(verbose_name="Payment Status",max_length=100)

    def __str__(self):
        return self.name