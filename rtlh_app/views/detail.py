from django.shortcuts import render, redirect
from django.views import View
from rtlh_app.models import data_rumah
from django.db import transaction
from django.contrib import messages
from django.urls import reverse


class DetailDaftarViews(View):
    def get(self, request, id_daftar):
        data_daftar = data_rumah.objects.get(id=id_daftar)
        data = {
            'data_daftar' : data_daftar
        }
        return render(request, 'daftar/detail.html', data)
    
    def post(self, request, id_daftar):
        frm_no_kk = request.POST.get('no_kk')
        frm_nik = request.POST.get('nik')
        frm_nama_kk = request.POST.get('nama_kk')
        frm_alamat = request.POST.get('alamat')
        frm_pekerjaan = request.POST.get('pekerjaan')
        frm_keterangan = request.POST.get('keterangan')
        frm_kriteria = request.POST.get('kriteria')
        frm_status_pengajuan = request.POST.get('status_pengajuan') 

        try:
            with transaction.atomic():
                insert = data_rumah.objects.get(id=id_daftar)
                insert.no_kk = frm_no_kk
                insert.nik = frm_nik
                insert.nama_kk = frm_nama_kk
                insert.alamat = frm_alamat
                insert.pekerjaan = frm_pekerjaan
                insert.keterangan = frm_keterangan
                insert.kriteria = frm_kriteria
                insert.status_pengajuan = frm_status_pengajuan
                insert.save()

                messages.success(request, f"Akun {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_app:daftar'))
                
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_app:daftar'))