from __future__ import unicode_literals

from django.db import models


class Customer_purchasedata(models.Model):
    customer_email = models.CharField(max_length =100)
    customer_name = models.CharField(max_length =100)
    customer_phone = models.CharField(max_length =100)
    product_name = models.CharField(max_length =100)
    product_price = models.IntegerField()
    quantity =models.IntegerField()
    confirmation_code = models.CharField(max_length =100)
    product_id = models.CharField(max_length =100)
    
    def __str__(self):

        return ' '.join([
            self.customer_name,
            
        ])
# Create your models here.
