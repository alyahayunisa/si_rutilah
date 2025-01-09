from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse


class KetViews(View):
    def get(self, request):
        data_ket = keterangan.objects.all()
        data = {
            'data_ket' : data_ket
        }
        return render(request, 'admin/ket/index.html', data)


class TambahViews(View):
    def get(self, request):
        data_kri = data_kriteria.objects.all()
        data = {
            'data_kri' : data_kri
        }
        return render(request, 'admin/ket/create.html', data)
    
    def post(self, request):
        frm_keterangan = request.POST.get('keterangan')
        frm_kerusakan = request.POST.get('kerusakan')
        frm_kri = request.POST.get('kriteria')
        print(frm_keterangan)
        
        try:
            with transaction.atomic():
                insert = keterangan()
                insert.keterangan = frm_keterangan
                insert.kerusakan = frm_kerusakan
                insert.kri = frm_kri
                insert.save()
                
                messages.success(request, f"form {insert.keterangan} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:keterangan'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.keterangan}")
            return redirect(reverse('rtlh_admin:keterangan'))

class HapusKetViews(View):
    def get(self, request, id_keterangan):
        try:
            with transaction.atomic():
                insert = keterangan.objects.get(id=id_keterangan)
                insert.delete()

                messages.success(request, f"Akun {insert.keterangan} berhasil dihapus")
                return redirect(reverse('rtlh_admin:keterangan'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.keterangan}")
            return redirect(reverse('rtlh_admin:keterangan'))