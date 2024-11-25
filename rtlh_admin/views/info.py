from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class InformasiViews(View):
    def get(self, request):
        data_info = informasi.objects.all()
        data = {
            'data_info' : data_info
        }
        return render(request, 'admin/informasi/index.html', data)
    
class TambahInfoViews(View):
    def get(self, request):
        data_info = informasi.objects.all()
        data = {
            'data_info' : data_info
        }
        return render(request, 'admin/informasi/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        
        
        try:
            with transaction.atomic():
                insert = informasi()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:informasi'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:informasi'))
        
class EditInfoViews(View):
    def get(self, request, id_info):
        data_info = informasi.objects.get(id=id_info)
        data = {
            'edit' : True,
            'data_info' : data_info
        }
        return render(request, 'admin/informasi/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')

        
        try:
            with transaction.atomic():
                insert = informasi()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:informasi'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:informasi'))        

class HapusInfoViews(View):
    def get(self, request, id_info):
        try:
            with transaction.atomic():
                insert = informasi.objects.get(id=id_info)
                insert.delete()

                messages.success(request, f"Akun {insert.judul} berhasil dihapus")
                return redirect(reverse('rtlh_admin:informasi'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:informasi'))
        