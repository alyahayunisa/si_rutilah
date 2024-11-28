from django.shortcuts import render, redirect
from django.views import View
from rtlh_app.models import data_rumah
from django.db.models import Q
from django.db import transaction
from django.contrib import messages
from django.urls import reverse



class DaftarViews(View):
    def get(self, request):
        query = request.GET.get('q', '')  # Ambil query dari parameter URL
        if query:
            # Filter data berdasarkan nama KK atau keterangan
            data_daftar = data_rumah.objects.filter(
                Q(nama_kk__icontains=query) | Q(keterangan__icontains=query)
            )
        else:
            data_daftar = data_rumah.objects.all()
        data = {
            'data_daftar' : data_daftar
        }
        return render(request, 'daftar/index.html', data)
    
        

class EditDaftarViews(View):
    def get(self, request, id_daftar):
        data_daftar = data_rumah.objects.get(id=id_daftar)
        data = {
            'edit' : True,
            'data_daftar' : data_daftar
        }
        return render(request, 'daftar/create.html', data)
    
    def post(self, request, id_daftar):
        frm_nama_kk = request.POST.get('nama_pemilik')
        frm_keterangan = request.POST.get('keterangan')
        frm_kriteria = request.POST.get('kriteria')

        try:
            with transaction.atomic():
                insert = data_rumah.objects.get(id=id_daftar)
                insert.nama_kk = frm_nama_kk
                insert.keterangan = frm_keterangan
                insert.kriteria = frm_kriteria
                insert.save()

                messages.success(request, f"Akun {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_app:daftar'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_app:daftar'))
        
class DeleteDaftarViews(View):
    def get(self, request, id_daftar):
        try:
            with transaction.atomic():
                insert = data_rumah.objects.get(id=id_daftar)
                insert.delete()

                messages.success(request, f"Akun {insert.nama_kk} berhasil dihapus")
                return redirect(reverse('rtlh_app:daftar'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_app:daftar'))
        

