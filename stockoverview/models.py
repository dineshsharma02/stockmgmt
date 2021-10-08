from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    operation = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=50)
    wheat = models.DecimalField(max_digits=5, decimal_places=2)
    rice = models.DecimalField(max_digits=5, decimal_places=2)
    combo = models.DecimalField(max_digits=2, decimal_places=0)
