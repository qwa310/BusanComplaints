from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# from .models import Student

# Create your views here.
def index(request):
    return render(request, "index.html")

def index2(request):
    return render(request,'index2.html')