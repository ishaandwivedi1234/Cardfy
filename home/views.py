from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse

# Create your views here.

def index(request):
    context = {
        "pageName":"index"
    }
    return render(request,'index.html',context)