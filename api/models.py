from django.db import models

# Create your models here.

class Vendors(models.Model):
    vendor_name = models.CharField(max_length=200)
    vendor_number = models.CharField(max_length=64)
    agreement_number = models.CharField(max_length=120)
    contract_status = models.CharField(max_length=64)   # moving this to ENUM (choices) in future
    contract_category = models.CharField(max_length=40)
    contract_date = models.DateField('contract_date')
    contract_expiry = models.DateField('contract_expiry')

    def __str__(self):
        return self.vendor_name
