from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class TipsrtlhViews(View):
    def get(self, request):
        data_tips = tips.objects.all()
        data = {
            'data_tips' : data_tips
        }
        return render(request, 'admin/tips/index.html', data)
    
class TambahTipsrtlhViews(View):
    def get(self, request):
        data_tips = tips.objects.all()
        data = {
            'data_tips' : data_tips
        }
        return render(request, 'admin/tips/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_icon = request.FILES.get('icon')
        
        try:
            with transaction.atomic():
                insert = tips()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.icon = frm_icon
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:tips'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:tips'))
        
class EditTipsrtlhViews(View):
    def get(self, request, id_tipsrtlh):
        data_tips = tips.objects.get(id=id_tipsrtlh)
        data = {
            'edit' : True,
            'data_tips' : data_tips,
        }
        return render(request, 'admin/tips/create.html', data)
    
    def post(self, request):
        frm_judul = request.POST.get('judul')
        frm_deskripsi = request.POST.get('deskripsi')
        frm_icon = request.FILES.get('icon')
        
        try:
            with transaction.atomic():
                insert = tips()
                insert.judul = frm_judul
                insert.deskripsi = frm_deskripsi
                insert.icon = frm_icon
                insert.save()
                
                messages.success(request, f"form {insert.judul} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:tips'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:tips'))
        
class HapusTipsrtlhViews(View):
    def get(self, request, id_tipsrtlh):
        try:
            with transaction.atomic():
                insert = tips.objects.get(id=id_tipsrtlh)
                insert.delete()

                messages.success(request, f"Akun {insert.judul} berhasil dihapus")
                return redirect(reverse('rtlh_admin:tips'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.judul}")
            return redirect(reverse('rtlh_admin:tips'))