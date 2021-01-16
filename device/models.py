from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Device(models.Model):
    device_name = models.CharField(max_length=64)
    device_type = models.CharField(max_length=64)
    device_company = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    device_price = models.DecimalField(max_digits=5 ,decimal_places=2)
    
    
    def __str__(self):
        return self.device_name