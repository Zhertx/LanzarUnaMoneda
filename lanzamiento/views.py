from django.shortcuts import render
import random

def tirar_moneda(request):
    resultado = random.choice(['Cara', 'Cruz'])
    return render(request, 'index.html', {'resultado': resultado})
