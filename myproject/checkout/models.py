from pyexpat import model
from django.db import models

# Create your models here.

class Orders(models.Model):
    userId=models.IntegerField()
    orderId=models.CharField(max_length=100)
    order_amount=models.BigIntegerField()
    order_date=models.DateTimeField(auto_now_add=True)