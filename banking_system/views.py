from django.shortcuts import render,redirect
from .models import customer,transfer
# Create your views here.
from django.db import transaction
from django.http import HttpResponse
from django.contrib import messages
@transaction.atomic
def moneyTransfer(request):
    # This code executes inside a transaction.
    if request.method=='POST' and 'reciverId' in request.POST and 'amount' in request.POST:
        From=customer.objects.get(id=int(request.POST.get('senderId')))
        To=customer.objects.get(id=int(request.POST.get('reciverId')))
        print(request.POST)
        amount=int(request.POST.get('amount'))
        if amount <= From.current_balence:
            T=transfer(send_from=From,send_to=To,amount=amount)
            T.save()
            From.current_balence-=amount
            To.current_balence+=amount
            From.save()
            To.save()
            return redirect(index)
            
        else:
            return HttpResponse('no sufficent balence')
    else: 
        sender_id=request.POST.get('senderId')
        sender=customer.objects.filter(id =int(sender_id)).first()
        recivers=customer.objects.exclude(id =int(sender_id))
        messages.error(request,'Please select Reciver')
        return render(request,'Second.html',{'sender':sender,'recivers': recivers})
        
    
    
def index(request):
    if request.method=='GET':
        return render(request,'home.html')
        
    else:
        senders=customer.objects.all()
        return render(request,'index.html',{'senders':senders})
    

def showProfile(request):
    
    #this takes you to watching profiles of people
    
    if request.method=='POST' and 'senderId' in request.POST:
        print(request.POST)
        sender_id=request.POST.get('senderId')
        if sender_id == 'Select Sender' :
            senders=customer.objects.all()
            messages.error(request, 'Please select customer.')
            return render(request,'index.html',{'senders':senders})
    
        else:
            sender=customer.objects.filter(id =int(sender_id)).first()
            return render(request,'customer.html',{'customer':sender})
            
        
   # this takes you yo select recivers page
   
    else:
        print(request.POST)
        sender_id=request.POST.get('customerId')
        sender=customer.objects.filter(id =int(sender_id)).first()
        recivers=customer.objects.exclude(id =int(sender_id))
        return render(request,'Second.html',{'sender':sender,'recivers': recivers})
        
 
 