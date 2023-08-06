from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def proyectos(request):
  context={
  }
  return render(request,'proyectos/proyectos.html',context)