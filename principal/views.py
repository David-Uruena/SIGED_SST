from django.shortcuts import render

def holamundo(request):
    nombre = "David"
    apellido = "Urueña"
    tel = "31323545"
    context={
        'nombres':nombre,
        'apellidos': apellido,
        'telefono': tel
    }
    return render(request, 'index.html', context)
