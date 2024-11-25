from django.db import models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    locations=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),("Mobile Phones","Mobile Phones")))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

def __str__(self):
    return self.name+'--'+self.location


class Employee(models.Model):
    Emp_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    phone=models.CharField(max_length=50)
    about=models.TextField(max_length=200)
    Position=models.CharField(max_length=100,choices=(('Manager','manager'),('software developer','sde'),
    ('project leader','prleader')
    ))
   
