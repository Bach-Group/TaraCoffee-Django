from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("about")

def HomePage(request):
    # return HttpResponse("This is HomePage")
    return render(request,'HomePage.html')