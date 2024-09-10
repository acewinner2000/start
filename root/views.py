from django.shortcuts import render
from .models import *


def home(request): 
    services = Services.objects.filter(status = True)
    trainer = Trainers.objects.filter(status = True)
    pricing = Pricing.objects.filter(status = True)
    special = SpecialServices.objects.filter(status = True)
    ask1 = ask.objects.filter(status = True)
    context = {
        "services":services
        ,"trainers":trainer
        ,"pricing":pricing
        ,"special":special
        ,"ask":ask1
    }

    return render(request, 'root/index.html',context=context)
def about(request):
    pass

def login(request):
    
    return render(request, 'root/login.html')