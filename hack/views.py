from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def verticals(request):
    return render(request, 'verticals.html')

def agriculture(request):
    return render(request, 'agriculture.html')

def banking(request):
    return render(request, 'banking.html')

def bd(request):
    return  render(request, 'bd.html')

def fintech(request):
    return render(request, 'fintech.html')

def hospitality(request):
    return render(request, 'hospitality.html')

def hr(request):
    return render(request, 'hr.html')

def insurance(request):
    return render(request, 'insurance.html')

def inventory(request):
    return render(request, 'inventory.html')

def manufacturing(request):
    return render(request, 'manufacturing.html')

def marketing(request):
    return render(request, 'marketing.html')

def pharma(request):
    return render(request, 'pharma.html')

def retail(request):
    return render(request, 'retail.html')

def telecom(request):
    return render(request, 'telecom.html')

def travel(request):
    return render(request, 'travel.html')

def utilities(request):
    return render(request, 'utilities.html')