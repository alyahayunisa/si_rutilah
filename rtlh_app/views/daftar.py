from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import verifikasi
from django.db.models import Q
from django.db import transaction
from django.contrib import messages
from django.urls import reverse



class DaftarViews(View):
    def get(self, request):
        data_verif = verifikasi.objects.all()
        data = {
            'data_verif' : data_verif
        }
        return render(request, 'daftar/index.html', data)
    
        


        

