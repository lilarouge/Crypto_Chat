import json
from django.shortcuts import render, redirect
from django.views import View
from customer.models import OrderModel
# Create your views here.
def shalom(request):

    return render(request, 'shalom.html')

def robot(request):

    return render(request, 'aiortc/examples/server/index.html')

