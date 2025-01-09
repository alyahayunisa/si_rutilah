from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class FnKrirtlhViews(View):
    def get(self, request):
        data_krirtlh = kriteriartlh.objects.all()
        data = {
            'data_krirtlh' : data_krirtlh
        }
        return render(request, 'admin/kriteriartlh/index.html', data)
    
class TambahKrirtlhViews(View):
    def get(self, request):
        data_krirtlh = kriteriartlh.objects.all()
        data = {
            'data_krirtlh' : data_krirtlh
        }
        return render(request, 'admin/kriteriartlh/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_icon = request.FILES.get('icon')
        
        try:
            with transaction.atomic():
                insert = kriteriartlh()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.icon = frm_icon
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:kriteriartlh'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:kriteriartlh'))
        
class EditKrirtlhViews(View):
    def get(self, request, id_krirtlh):
        data_krirtlh = kriteriartlh.objects.get(id=id_krirtlh)
        data = {
            'edit' : True,
            'data_krirtlh' : data_krirtlh,
        }
        return render(request, 'admin/kriteriartlh/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_icon = request.FILES.get('icon')
        
        try:
            with transaction.atomic():
                insert = kriteriartlh()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.icon = frm_icon
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:kriteriartlh'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:kriteriartlh'))
        
class HapusKrirtlhViews(View):
    def get(self, request, id_krirtlh):
        try:
            with transaction.atomic():
                insert = kriteriartlh.objects.get(id=id_krirtlh)
                insert.delete()

                messages.success(request, f"Akun {insert.judul} berhasil dihapus")
                return redirect(reverse('rtlh_admin:kriteriartlh'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:kriteriartlh'))