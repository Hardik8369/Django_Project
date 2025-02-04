from django.db import models

# Create your models here.
class StudentDepartment(models.Model):
    DEPT_NAME=models.CharField(max_length=100)
    DEPT_DESC=models.CharField(max_length=1000)

class Employee_Table(models.Model):
    EMP_NAME=models.CharField(max_length=500)
    EMP_DESI=models.CharField(max_length=500)
    EMP_PLACE=models.CharField(max_length=500)