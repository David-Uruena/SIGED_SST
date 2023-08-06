from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def listachequeo(request):
  context={
  }
  return render(request,'listachequeo/listachequeo.html',context)