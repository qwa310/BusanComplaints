from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# from .models import Student

# Create your views here.
def index(request):
    return render(request, "index.html")

def index2(request):
    return render(request,'index2.html')
def complaint_input_form(request):
    return render(request,'complaint_input.html')
def complaint_input(request):
    area = request.POST['area']
    title = request.POST['title']
    text = request.POST['text']
    qs = {'area' : area , 'title':title , 'text' : text}
    print(qs)
    print(qs['area'], qs['title'] , qs['text'])
    return render(request , 'result.html',qs)
def complaint_output(request):
    pass