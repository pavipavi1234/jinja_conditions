from django.shortcuts import render

# Create your views here.
def wish(request):
    return render(request,'wish.html')
def conditions(request):
    d={'a':20,'b':40}
    return render(request,'conditions.html',d)
