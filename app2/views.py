from django.shortcuts import render

# Create your views here.
def login1(request):
    return render(request,'login1.html') 

def login2(request):
    return render(request, 'login2.html')

def login3(request):
    return render(request, 'login3.html')

def card(request):
    return render(request, 'Card.html')