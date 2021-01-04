from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=53,unique=True,null=False)
    current_balence=models.IntegerField()

class transfer(models.Model):
    id=models.AutoField(primary_key=True)
    send_from=models.ForeignKey(customer,on_delete=models.CASCADE,related_name='sender')
    send_to=models.ForeignKey(customer,on_delete=models.CASCADE,related_name='reciver')
    date=models.DateField(default=timezone.localdate())
    time=models.TimeField(default=timezone.now())
    amount=models.IntegerField(null=False,default=0)
    