from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class UndangViews(View):
    def get(self, request):
        data_undang = undang_undang.objects.all()
        data = {
            'data_undang' : data_undang
        }
        return render(request, 'admin/undang/index.html', data)
    
class TambahUndangViews(View):
    def get(self, request):
        data_undang = undang_undang.objects.all()
        data = {
            'data_undang' : data_undang
        }
        return render(request, 'admin/undang/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_img_uu = request.FILES.get('img_uu')
        
        try:
            with transaction.atomic():
                insert = undang_undang()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.img_uu = frm_img_uu
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:undang'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:undang'))
        
class EditUndangViews(View):
    def get(self, request, id_undang):
        data_undang = undang_undang.objects.get(id=id_undang)
        data = {
            'edit' : True,
            'data_undang' : data_undang,
        }
        return render(request, 'admin/undang/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_img_uu = request.FILES.get('img_uu')
        
        try:
            with transaction.atomic():
                insert = undang_undang()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.img_uu = frm_img_uu
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:undang'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:undang'))
        
class HapusUndangViews(View):
    def get(self, request, id_undang):
        try:
            with transaction.atomic():
                insert = undang_undang.objects.get(id=id_undang)
                insert.delete()

                messages.success(request, f"Akun {insert.judul} berhasil dihapus")
                return redirect(reverse('rtlh_admin:undang'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:undang'))