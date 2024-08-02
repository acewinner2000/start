from django.shortcuts import render
from .models import *


def home(request):
    ser=service.objects.filter(status=True)
    return render(request,'root/index.html',context={'service':ser})

def sp(request):
    so=so.objects.filter(status=True)
    return render(request,'root/index.html',context={'so':so})
