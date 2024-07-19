from django.contrib import admin

# Register your models here.
from  .models import department,student
admin.site.register(department)
admin.site.register(student)
