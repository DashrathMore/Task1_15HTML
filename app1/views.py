from django.shortcuts import render

# Create your views here.
def table(request):
    return render (request, 'table.html')

def table1(request):
    return render(request, 'table1.html')

def table2(request):
    return render(request, 'table2.html')

def table3(request):
    return render(request, 'table3.html')

def table4(request):
    return render(request, 'table4.html')

def table5(request):
    return render(request, 'table5.html')

def home(request):
    return render(request, 'landingpage.html')