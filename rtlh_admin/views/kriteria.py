from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import data_kriteria
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class KriteriaViews(View):
    def get(self, request):
        data_kri = data_kriteria.objects.all()
        data = {
            'data_kri' : data_kri
        }
        return render(request, 'admin/kriteria/index.html', data)
    

class CreateKriteriaViews(View):
    def get(self, request):
        data_kri = data_kriteria.objects.all()
        data = {
            'data_kri' : data_kri
        }
        return render(request, 'admin/kriteria/create.html', data)
    
    def post(self, request):
        frm_kriteria = request.POST.get('kriteria')
        frm_desk_singkat = request.POST.get('desk_singkat')
        frm_desk_detail = request.POST.get('desk_detail')
        frm_desk_full = request.POST.get('desk_full')
        frm_img_tipe = request.FILES.get('img_tipe')
        print(frm_kriteria)
        print(frm_img_tipe)
        
        try:
            with transaction.atomic():
                insert = data_kriteria()
                insert.kriteria = frm_kriteria
                insert.desk_singkat = frm_desk_singkat
                insert.desk_detail = frm_desk_detail
                insert.desk_full = frm_desk_full
                insert.img_tipe = frm_img_tipe
                insert.save()
                
                messages.success(request, f"form {insert.kriteria} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:kriteria'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.kriteria}")
            return redirect(reverse('rtlh_admin:kriteria'))
    

class EditKriteriaViews(View):
    def get(self, request, id_kriteria):
        data_kri = data_kriteria.objects.get(id=id_kriteria)
        data = {
            'edit': True,          # Menandakan bahwa ini adalah halaman edit
            'data_kri': data_kri   # Mengirimkan data kriteria untuk di-edit
        }
        
        return render(request, 'admin/kriteria/create.html', data)
    
    def post(self, request):
        # Ambil data yang di-submit dari form
        frm_kriteria = request.POST.get('kriteria')
        frm_desk_singkat = request.POST.get('desk_singkat')
        frm_desk_detail = request.POST.get('desk_detail')
        frm_desk_full = request.POST.get('desk_full')
        frm_img_tipe = request.FILES.get('img_tipe')
        print(frm_kriteria)
        
        try:
            with transaction.atomic(): 
                insert = data_kriteria()
                insert.kriteria = frm_kriteria
                insert.desk_singkat = frm_desk_singkat
                insert.desk_detail = frm_desk_detail
                insert.desk_full = frm_desk_full
                insert.img_tipe = frm_img_tipe
                insert.save()

                messages.success(request, f"form {insert.kriteria} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:kriteria'))
        
        except Exception as e:
            print('Error:', e)
            messages.error(request, "Gagal mengubah data kriteria")
            return redirect(reverse('rtlh_admin:kriteria'))  

class HapusKriteriaViews(View):
    def get(self, request, id_kriteria):
        try:
            with transaction.atomic():
                insert = data_kriteria.objects.get(id=id_kriteria)
                insert.delete()

                messages.success(request, f"Akun {insert.kriteria} berhasil dihapus")
                return redirect(reverse('rtlh_admin:kriteria'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.kriteria}")
            return redirect(reverse('rtlh_admin:kriteria'))

    
    
