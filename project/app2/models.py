from django.db import models

# Create your models here.
from django.db import models

class vhicle(models.Model):
    vhicle_no=models.IntegerField(unique=True)
    model_name=models.CharField(max_length=50)

    def __str__(self):
        return str( self.vhicle_no)
class coustmer(models.Model):
    coustmer_name=models.CharField(max_length=50)
    coustmer_city=models.CharField(max_length=50,null=True)
    coustmer_email=models.EmailField()
    coustmer_no=models.ManyToManyField(vhicle)
