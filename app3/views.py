from django.shortcuts import render

# Create your views here.
def animation(request):
    return render(request, 'animation.html')

def animation2(request):
    return render(request, 'animation2.html')

def animation3(request):
    return render(request, 'annimation3.html')