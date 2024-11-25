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
    
    
class HapusUserViews(View):
    def get(self, request, id_user):
        try:
            with transaction.atomic():
                insert = Master_User.objects.get(id=id_user)
                insert.delete()

                messages.success(request, f"Akun {insert.username} berhasil dihapus")
                return redirect(reverse('rtlh_admin:user'))
            
        except Exception as e:
            print('Error akun', e)
            messages.error(request, f"Gagal menambahkan data {insert.username}")
            return redirect(reverse('rtlh_admin:user'))
