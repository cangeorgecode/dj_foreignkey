from django.shortcuts import render
from customers.models import *

def index(request):
    customers = Customer.objects.all()
    businesses = Business.objects.all()
    context = {
        'customers': customers,
        'businesses': businesses,
        }
    return render(request, 'customers/index.html', context)
