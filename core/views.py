
#conding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def produto(request):
    return render(request,'produto.html')
def produtos(request):
    return render(request,'produtos.html')
def contato(request):
    return render(request,'contato.html')
