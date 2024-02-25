from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tax_rate = 0.15

def index(request):
    return HttpResponse("Hello and welcome to this tax calculator!")

def anyNumber(request, price):
    return HttpResponse(f"The total with tax is: ${int(price) + (int(price)*tax_rate)}")

def taxrate(request):
    return render(request, "Lab4App/taxrate.html", {
        "tax_rate": tax_rate*100
    })