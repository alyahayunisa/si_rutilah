from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class RtlhViews(View):
    def get(self, request):
        data_rumahrtlh = data_rtlh.objects.all()
        data = {
            'data_rumahrtlh' : data_rumahrtlh
        }
        return render(request, 'admin/rtlh/index.html', data)
    

    
class TambahRtlhViews(View):
    def get(self, request):
        data_daftar = data_rumah.objects.all()
        data_kri = data_kriteria.objects.all()
        data = {
            'data_daftar' : data_daftar,
            'data_kri' : data_kri
        }
        return render(request, 'admin/rtlh/create.html', data)
    
    def post(self, request):
        frm_nama_kk = request.POST.get('nama_kk')
        frm_status_tanah = request.POST.get('status_tanah')
        frm_status_kepemilikan = request.POST.get('status_kepemilikan')
        frm_luas_tanah = request.POST.get('luas_tanah')
        frm_status_rumah = request.POST.get('status_rumah')
        frm_luas_bangunan = request.POST.get('luas_bangunan')
        frm_kondisi_pondasi = request.POST.get('kondisi_pondasi')
        frm_kondisi_atap = request.POST.get('kondisi_atap')
        frm_kondisi_lantai = request.POST.get('kondisi_lantai')
        frm_kondisi_dinding = request.POST.get('kondisi_dinding')
        frm_kondisi_ventilasi = request.POST.get('kondisi_ventilasi')
        frm_kondisi_toilet = request.POST.get('kondisi_toilet')
        frm_sumber_airbersih = request.POST.get('sumber_airbersih')
        frm_sumber_lisrik = request.POST.get('sumber_listrik')
        frm_kriteria = request.POST.get('kriteria')
        frm_img_rumah = request.FILES.get('img_rumah')
        frmisi = data_rumah.objects.get(id=frm_nama_kk)
        print(frm_nama_kk)
        
        try:
            with transaction.atomic():
                insert = data_rtlh()
                insert.nama_kk = frmisi
                insert.status_tanah = frm_status_tanah
                insert.status_kepemilikan = frm_status_kepemilikan
                insert.luas_tanah = frm_luas_tanah
                insert.status_rumah = frm_status_rumah
                insert.luas_bangunan = frm_luas_bangunan                
                insert.kondisi_pondasi = frm_kondisi_pondasi
                insert.kondisi_atap = frm_kondisi_atap
                insert.kondisi_lantai = frm_kondisi_lantai
                insert.kondisi_dinding = frm_kondisi_dinding
                insert.kondisi_ventilasi = frm_kondisi_ventilasi
                insert.kondisi_toilet = frm_kondisi_toilet
                insert.sumber_airbersih = frm_sumber_airbersih
                insert.sumber_listrik = frm_sumber_lisrik
                insert.kriteria = frm_kriteria
                insert.img_rumah = frm_img_rumah
                insert.save()
                
                messages.success(request, f"form {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:rtlh'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:rtlh'))
        


class UbahRtlhViews(View):
    def get(self, request, id_rtlh):
        data_rumahrtlh = data_rtlh.objects.get(id=id_rtlh)
        data = {
            'edit' : True,
            'data_rumahrtlh' : data_rumahrtlh
        }
        return render(request, 'admin/rtlh/create.html', data)
    
    def post(self, request):
       def post(self, request):
        frm_nama_kk = request.POST.get('nama_kk')
        frm_status_tanah = request.POST.get('status_tanah')
        frm_status_kepemilikan = request.POST.get('status_kepemilikan')
        frm_luas_tanah = request.POST.get('luas_tanah')
        frm_status_rumah = request.POST.get('status_rumah')
        frm_luas_bangunan = request.POST.get('luas_bangunan')
        frm_kondisi_pondasi = request.POST.get('kondisi_pondasi')
        frm_kondisi_atap = request.POST.get('kondisi_atap')
        frm_kondisi_lantai = request.POST.get('kondisi_lantai')
        frm_kondisi_dinding = request.POST.get('kondisi_dinding')
        frm_kondisi_ventilasi = request.POST.get('kondisi_ventilasi')
        frm_kondisi_toilet = request.POST.get('kondisi_toilet')
        frm_sumber_airbersih = request.POST.get('sumber_airbersih')
        frm_sumber_lisrik = request.POST.get('sumber_listrik')
        frm_kriteria = request.POST.get('kriteria')
        frm_img_rumah = request.FILES.get('img_rumah')
        frmisi = data_rumah.objects.get(id=frm_nama_kk)
        print(frm_nama_kk)
        
        try:
            with transaction.atomic():
                insert = data_rtlh()
                insert.nama_kk = frmisi
                insert.status_tanah = frm_status_tanah
                insert.status_kepemilikan = frm_status_kepemilikan
                insert.luas_tanah = frm_luas_tanah
                insert.status_rumah = frm_status_rumah
                insert.luas_bangunan = frm_luas_bangunan                
                insert.kondisi_pondasi = frm_kondisi_pondasi
                insert.kondisi_atap = frm_kondisi_atap
                insert.kondisi_lantai = frm_kondisi_lantai
                insert.kondisi_dinding = frm_kondisi_dinding
                insert.kondisi_ventilasi = frm_kondisi_ventilasi
                insert.kondisi_toilet = frm_kondisi_toilet
                insert.sumber_airbersih = frm_sumber_airbersih
                insert.sumber_listrik = frm_sumber_lisrik
                insert.kriteria = frm_kriteria
                insert.img_rumah = frm_img_rumah
                insert.save()
                
                messages.success(request, f"form {insert.nama_kk} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:rtlh'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:rtlh'))
        
class HapusRtlhViews(View):
    def get(self, request, id_rtlh):
        try:
            with transaction.atomic():
                insert = data_rtlh.objects.get(id=id_rtlh)
                insert.delete()

                messages.success(request, f"Akun {insert.nama_kk} berhasil dihapus")
                return redirect(reverse('rtlh_admin:rtlh'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.nama_kk}")
            return redirect(reverse('rtlh_admin:rtlh'))