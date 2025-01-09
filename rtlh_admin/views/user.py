from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import Master_User
from django.db import transaction
from django.contrib import messages
from django.urls import reverse


class UserViews(View):
    def get(self, request):
        data_User = Master_User.objects.all()
        data = {
            'data_user' : data_User
        }
        return render(request, 'admin/user/index.html', data)
    
class TambahUserViews(View):
    def get(self, request):
        data_user = Master_User.objects.all()
        data = {
            'data_user' : data_user
        }
        return render(request, 'admin/user/create.html', data)
    
    def post(self, request):
        frm_email = request.POST.get('email')
        frm_username = request.POST.get('username')
        frm_first_name = request.POST.get('first_name')
        frm_last_name = request.POST.get('last_name')
        frm_phone = request.POST.get('phone')
        frm_role = request.POST.get('role')
        frm_date_of_birth = request.POST.get('date_of_birth')
        frm_password = request.POST.get('password')
        frm_confirm_password = request.POST.get('confirm_password')

        if frm_password != frm_confirm_password:
            messages.erorr(request,"password dan confirm password tidak sesuai") 
            return redirect(reverse('rtlh_admin:user'))


        
        try:
            with transaction.atomic():
                insert = Master_User()
                insert.email = frm_email
                insert.username = frm_username
                insert.first_name = frm_first_name
                insert.last_name = frm_last_name
                insert.phone = frm_phone
                insert.role = frm_role
                insert.date_of_birth = frm_date_of_birth
                insert.set_password(frm_password)
                insert.save()
                
                messages.success(request, f"form {insert.email} berhasil ditambahkan")
                return redirect(reverse('rtlh_admin:user'))
            
            
        except Exception as e:
            print('error akun', e)
            messages.error(request, f"gagal menambahkan data {insert.email}")
            return redirect(reverse('rtlh_admin:user'))
    
    
class HapusUserViews(View):
    def get(self, request, id_user):
        try:
            with transaction.atomic():
                # Ambil user berdasarkan id_user yang diterima dari URL
                user = Master_User.objects.get(id=id_user)
                user.delete()

                messages.success(request, f"Akun {user.username} berhasil dihapus")
                return redirect('rtlh_admin:user')  # Pastikan 'rtlh_admin:user' adalah nama URL yang benar
            
        except Master_User.DoesNotExist:
            messages.error(request, "Akun yang ingin dihapus tidak ditemukan")
            return redirect('rtlh_admin:user')
        
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menghapus data {user.username}")
            return redirect('rtlh_admin:user')
