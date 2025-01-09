from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class KontakhubViews(View):
    def get(self, request):
        data_kontak = kontak.objects.all()
        data = {
            'data_kontak' : data_kontak
        }
        return render(request, 'admin/kontak/index.html', data)
    
class TambahKontakhubViews(View):
    def get(self, request):
        data_kontak = kontak.objects.all()
        data = {
            'data_kontak' : data_kontak
        }
        return render(request, 'admin/kontak/create.html', data)
    
    def post(self, request):
        frm_alamat = request.POST.get('alamat')
        frm_no_hp = request.POST.get('no_hp')
        frm_latitude = request.POST.get('latitude')  # Ambil latitude dari form
        frm_longitude = request.POST.get('longitude')
        
        try:
            with transaction.atomic():
                insert = kontak()
                insert.alamat = frm_alamat
                insert.no_hp = frm_no_hp
                insert.latitude = (frm_latitude) 
                insert.longitude = (frm_longitude) 
                insert.save()
                
                messages.success(request, f"form {insert.alamat} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:kontak'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.alamat}")
            return redirect(reverse('rtlh_admin:kontak'))
        
class EditKontakhubViews(View):
    def get(self, request, id_kontakhub):
        data_kontak = kontak.objects.get(id=id_kontakhub)
        data = {
            'edit' : True,
            'data_kontak' : data_kontak,
        }
        return render(request, 'admin/kontak/create.html', data)
    
    def post(self, request):
        frm_alamat = request.POST.get('alamat')
        frm_no_hp = request.POST.get('no_hp')
        frm_latitude = request.POST.get('latitude')  # Ambil latitude dari form
        frm_longitude = request.POST.get('longitude')
        
        try:
            with transaction.atomic():
                insert = kontak()
                insert.alamat = frm_alamat
                insert.no_hp = frm_no_hp
                insert.latitude = (frm_latitude) 
                insert.longitude = (frm_longitude) 
                insert.save()
                
                messages.success(request, f"form {insert.alamat} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:kontak'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.alamat}")
            return redirect(reverse('rtlh_admin:kontak'))
        
class HapusKontakhubViews(View):
    def get(self, request, id_kontakhub):
        try:
            with transaction.atomic():
                insert = kontak.objects.get(id=id_kontakhub)
                insert.delete()

                messages.success(request, f"Akun {insert.alamat} berhasil dihapus")
                return redirect(reverse('rtlh_admin:kontak'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.alamat}")
            return redirect(reverse('rtlh_admin:kontak'))