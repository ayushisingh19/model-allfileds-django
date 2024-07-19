from django.db import models

class Aadhar(models.Model):
    aadhar_no=models.IntegerField(unique=True)
    created_date=models.DateField()
    created_by=models.CharField(max_length=50)
    def __str__(self):
        return str( self.aadhar_no)
class student(models.Model):
    str_name=models.CharField(max_length=50)
    str_city=models.CharField(max_length=50,null=True)
    str_email=models.EmailField()
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)