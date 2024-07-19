from django.db import models


# Create your models here.
class department (models.Model):
    dep_name=models.CharField(max_length=50)
    dep_discription=models.CharField(max_length=150)
    def __str__(self):
        return self.dep_name
class student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField(max_length=50,null=True)
    stu_contact=models.IntegerField()
    dep_name=models.ForeignKey(department,on_delete=models.CASCADE)
