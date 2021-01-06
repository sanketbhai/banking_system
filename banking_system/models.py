from django.db import models
import django.utils.timezone as timezone
from datetime import datetime
# Create your models here.
class customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=53,unique=True,null=False)
    current_balence=models.IntegerField()
    def __str__(self): 

         return f"{ self.id } , { self.name }"
class transfer(models.Model):
    id=models.AutoField(primary_key=True)
    send_from=models.ForeignKey(customer,on_delete=models.CASCADE,related_name='sender')
    send_to=models.ForeignKey(customer,on_delete=models.CASCADE,related_name='reciver')
    date=models.DateField(default=timezone.now)
    time=models.TimeField(default=datetime.now())
    amount=models.IntegerField(null=False,default=0)
    def __str__(self):
        return f"{self.send_from} --> { self.send_to}"