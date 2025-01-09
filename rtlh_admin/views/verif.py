from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class VerifViews(View):
    def get(self, request):
        data_verif = verifikasi.objects.all()
        data = {
            'data_verif' : data_verif
        }
        return render(request, 'admin/verifikasi/index.html', data)
    
class TambahVerifViews(View):
    def get(self, request):
        data_daftar = data_rumah.objects.all()
        data = {
            'data_daftar' : data_daftar
        }
        return render(request, 'admin/verifikasi/create.html', data)
    
    def post(self, request):
        frm_nama_kk = request.POST.get('nama_kk')
        frm_tanggal_verifikasi = request.POST.get('tanggal_verifikasi')
        frm_status_pengajuan = request.POST.get('status_pengajuan')
        frm_alasan = request.POST.get('alasan')
        frmisi = data_rumah.objects.get(id=frm_nama_kk)
        print(frm_tanggal_verifikasi)
        print(frm_status_pengajuan)
        print(frm_alasan)
        
        try:
            with transaction.atomic():
                insert = verifikasi()
                insert.nama_kk = frmisi
                insert.tanggal_verifikasi = frm_tanggal_verifikasi
                insert.status_pengajuan = frm_status_pengajuan
                insert.alasan = frm_alasan
                insert.save()
                
                messages.success(request, f"form {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:verifikasi'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:verifikasi'))
    
class UbahVerifViews(View):
    def get(self, request, id_verif):
        data_verif = verifikasi.objects.get(id=id_verif)
        data_daftar = data_rumah.objects.all()
        data = {
            'edit' : True,
            'data_verif' : data_verif,
            'data_daftar' : data_daftar
            
        }
        return render(request, 'admin/verifikasi/create.html', data)
    
    def post(self, request):
        frm_nama_kk = request.POST.get('nama_kk')
        frm_tanggal_verifikasi = request.POST.get('tanggal_verifikasi')
        frm_status_pengajuan = request.POST.get('status_pengajuan')
        frm_alasan = request.POST.get('alasan')
        frmisi = data_rumah.objects.get(id=frm_nama_kk)
        print(frm_tanggal_verifikasi)
        print(frm_status_pengajuan)
        print(frm_alasan)
        
        try:
            with transaction.atomic():
                insert = verifikasi()
                insert.nama_kk = frmisi
                insert.tanggal_verifikasi = frm_tanggal_verifikasi
                insert.status_pengajuan = frm_status_pengajuan
                insert.alasan = frm_alasan
                insert.save()
                
                messages.success(request, f"form {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:verifikasi'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:verifikasi'))
        
class HapusVerifViews(View):
    def get(self, request, id_verif):
        try:
            with transaction.atomic():
                insert = verifikasi.objects.get(id=id_verif)
                insert.delete()

                messages.success(request, f"Akun {insert.nama_kk} berhasil dihapus")
                return redirect(reverse('rtlh_admin:verifikasi'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:verifikasi'))
        