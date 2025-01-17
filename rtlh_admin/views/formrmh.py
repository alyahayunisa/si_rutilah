from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class FormRmhViews(View):
    def get(self, request):
        data_daftar = data_rumah.objects.all()
        data = {
            'data_daftar' : data_daftar
        }
        return render(request, 'admin/form/rumah.html', data)
    
    
    def post(self, request):
        frm_no_kk = request.POST.get('no_kk')
        frm_nik = request.POST.get('nik')
        frm_nama_kk = request.POST.get('nama_kk')
        frm_pendidikan = request.POST.get('pendidikan')
        frm_jenis_kelamin = request.POST.get('jenis_kelamin')
        frm_tempat_lahir = request.POST.get('tempat_lahir')
        frm_tanggal_lahir = request.POST.get('tanggal_lahir')
        frm_agama = request.POST.get('agama') 
        frm_alamat_lengkap = request.POST.get('alamat_lengkap')
        frm_kelurahan = request.POST.get('kelurahan')
        frm_jumlah_anggota = request.POST.get('jumlah_anggota')
        frm_no_hp = request.POST.get('no_hp')
        frm_pekerjaan = request.POST.get('pekerjaan') 
        frm_penghasilan = request.POST.get('penghasilan')
        frm_latitude = request.POST.get('latitude')  # Ambil latitude dari form
        frm_longitude = request.POST.get('longitude')
        print(frm_no_kk)
        
        try:
            with transaction.atomic():
                insert = data_rumah()
                insert.no_kk = frm_no_kk
                insert.nik = frm_nik
                insert.nama_kk = frm_nama_kk
                insert.pendidikan = frm_pendidikan
                insert.jenis_kelamin = frm_jenis_kelamin
                insert.tempat_lahir = frm_tempat_lahir
                insert.tanggal_lahir = frm_tanggal_lahir
                insert.agama = frm_agama
                insert.alamat_lengkap = frm_alamat_lengkap
                insert.kelurahan = frm_kelurahan
                insert.jumlah_anggota = frm_jumlah_anggota
                insert.no_hp = frm_no_hp
                insert.pekerjaan = frm_pekerjaan
                insert.penghasilan = frm_penghasilan
                insert.latitude = frm_latitude
                insert.longitude = frm_longitude 
                insert.save()
                
                messages.success(request, f"form {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:dashboard'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:dashboard'))


