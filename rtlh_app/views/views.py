from django.shortcuts import render



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