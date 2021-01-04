from django.shortcuts import render,redirect
from .models import customer,transfer
# Create your views here.
from django.db import transaction
from django.http import HttpResponse

@transaction.atomic
def reciver(request):
    # This code executes inside a transaction.
    From=customer.objects.get(id=int(request.POST.get('sender_id')))
    To=customer.objects.get(id=int(request.POST.get('s')))
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
        HttpResponse('nosufficent balence')
    
    
def index(request):
    if request.method=='POST':
        a=request.POST.get('s')
        print(request.POST)
        sender=customer.objects.filter(id =int(a)).first()
        recivers=customer.objects.exclude(id =int(a))
        print(recivers)
        
        return render(request,'Second.html',{'recivers':recivers,'sender':sender})
 
    else:
        senders=customer.objects.all()
        return render(request,'index.html',{'senders':senders})
    
  
    