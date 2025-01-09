from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class ProfileViews(View):
    def get(self, request):
        user = Master_User.objects.all()
        data = {
            'profile': user,  # Ambil data pengguna dari request.user
        }
        return render(request, 'admin/akun/profile.html', data)