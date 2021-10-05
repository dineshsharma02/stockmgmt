from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Students_Strength5(models.Model):
    class1 = models.DecimalField(max_digits=3, decimal_places=0)
    class2 = models.DecimalField(max_digits=3, decimal_places=0)
    class3 = models.DecimalField(max_digits=3, decimal_places=0)
    class4 = models.DecimalField(max_digits=3, decimal_places=0)
    class5 = models.DecimalField(max_digits=3, decimal_places=0)
    
class Students_Strength5Admin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # if there's already an entry, do not allow adding
    count = Students_Strength5.objects.all().count()
    if count == 0:
      return True

    return False


class Students_Strength8(models.Model):
    class6 = models.DecimalField(max_digits=3, decimal_places=0)
    class7 = models.DecimalField(max_digits=3, decimal_places=0)
    class8 = models.DecimalField(max_digits=3, decimal_places=0)


   

