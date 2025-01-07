from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import KontenPeraturanForm
from .models import KontenPeraturan



def beranda(request):
    return render(request, 'beranda.html')

def daftar(request):
    return render(request, 'daftar.html')

def informasi(request):
    return render(request, 'informasi.html')

def kriteria(request):
    return render(request, 'kriteria.html')

def kontak(request):
    return render(request,'kontak.html')

