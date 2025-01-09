from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class SekilasInfoViews(View):
    def get(self, request):
        data_sekilas = sekilas_info.objects.all()
        data = {
            'data_sekilas' : data_sekilas
        }
        return render(request, 'admin/sekilas/index.html', data)
    
class TambahSekilasViews(View):
    def get(self, request):
        data_sekilas = sekilas_info.objects.all()
        data = {
            'data_sekilas' : data_sekilas
        }
        return render(request, 'admin/sekilas/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_img_info = request.FILES.get('img_info')
        
        try:
            with transaction.atomic():
                insert = sekilas_info()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.img_uu = frm_img_info
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:sekilas'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:sekilas'))
        
class EditSekilasViews(View):
    def get(self, request, id_sekilas):
        data_sekilas = sekilas_info.objects.get(id=id_sekilas)
        data = {
            'edit' : True,
            'data_sekilas' : data_sekilas,
        }
        return render(request, 'admin/sekilas/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_img_info = request.FILES.get('img_info')
        
        try:
            with transaction.atomic():
                insert = sekilas_info()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.img_uu = frm_img_info
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:sekilas'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:sekilas'))
        
class HapusSekilasViews(View):
    def get(self, request, id_sekilas):
        try:
            with transaction.atomic():
                insert = sekilas_info.objects.get(id=id_sekilas)
                insert.delete()

                messages.success(request, f"Akun {insert.judul} berhasil dihapus")
                return redirect(reverse('rtlh_admin:sekilas'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:sekilas'))