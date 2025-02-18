from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse


class BantuanViews(View):
    def get(self, request):
        data_permohonan = permohonan.objects.all()
        data = {
            'data_permohonan' : data_permohonan
        }
        return render(request, 'admin/bantuan/index.html', data)
    
class TambahBantuanViews(View):
    def get(self, request):
        data_permohonan = permohonan.objects.all()
        nama_kk_terpakai = permohonan.objects.values_list('nama_kk_id', flat=True)
        data_daftar = data_rumah.objects.exclude(id__in=nama_kk_terpakai)
        data = {
            'data_daftar' : data_daftar,
            'data_permohonan' : data_permohonan
        }
        return render(request, 'admin/bantuan/create.html', data)
    
    def post(self, request):
        frm_nama_kk = request.POST.get('nama_kk')
        frm_img_ktp = request.FILES.get('img_ktp')
        frm_img_kk = request.FILES.get('img_kk')
        frm_img_rumah = request.FILES.get('img_rumah')
        frm_img_sertifikat = request.FILES.get('img_sertifikat')
        frmisi = data_rumah.objects.get(id=frm_nama_kk)
        print(frm_nama_kk)
        
        # Cek apakah nama_kk sudah ada dalam permohonan
        if permohonan.objects.filter(nama_kk_id=frm_nama_kk).exists():
            messages.error(request, "Nama KK sudah digunakan dalam permohonan sebelumnya.")
            return redirect(reverse('rtlh_admin:bantuan'))
        
        try:
            with transaction.atomic():
                insert = permohonan()
                insert.nama_kk = frmisi
                insert.img_ktp = frm_img_ktp
                insert.img_kk = frm_img_kk
                insert.img_rumah = frm_img_rumah
                insert.img_sertifikat = frm_img_sertifikat
                insert.save()
                
                messages.success(request, f"form {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:bantuan'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:bantuan'))
    
class UbahBantuanViews(View):
    def get(self, request, id_bantuan):
        data_permohonan = permohonan.objects.get(id=id_bantuan)
        data_daftar = data_rumah.objects.all()
        data = {
            'edit' : True,
            'data_permohonan' : data_permohonan,
            'data_daftar' : data_daftar
        }
        return render(request, 'admin/bantuan/create.html', data)
    
    
    
    def post(self, request):
        frm_no_kk = request.POST.get('no_kk')
        frm_nama_kk = request.POST.get('nama_kk')
        frm_img_ktp = request.FILES.get('img_ktp')
        frm_img_kk = request.FILES.get('img_kk')
        frm_img_rumah = request.FILES.get('img_rumah')
        frm_img_sertifikat = request.FILES.get('img_sertifikat')
        print(frm_no_kk)
        
        try:
            with transaction.atomic():
                insert = permohonan()
                insert.nama_kk = frm_nama_kk
                insert.img_ktp = frm_img_ktp
                insert.img_kk = frm_img_kk
                insert.img_rumah = frm_img_rumah
                insert.img_sertifikat = frm_img_sertifikat
                insert.save()
                
                messages.success(request, f"form {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:bantuan'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:bantuan'))
        
class DelBantuanViews(View):
    def get(self, request, id_bantuan):
        try:
            with transaction.atomic():
                insert = permohonan.objects.get(id=id_bantuan)
                insert.delete()

                messages.success(request, f"Akun {insert.nama_kk} berhasil dihapus")
                return redirect(reverse('rtlh_admin:bantuan'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:bantuan'))