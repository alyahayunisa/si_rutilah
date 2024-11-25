from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
#from support.support_function import truncate, convert_size, get_folder_size
from rtlh_admin.models import Master_User as m_user, ROLE_CHOICES
import shutil,os
from django.db import transaction
from django.db.models.functions import TruncMonth
from django.db.models import Sum, Count
from support.support_function import check_is_email
#from support import support_function as sup
#from support.support_function import admin_only
from django.db.models import Q, F

class LoginViews(View):
    def get(self, request):
        data = {
            'page_title': 'Login',
            #'breadcumb': [{'title': 'SIMDIKOAP', 'url':reverse('app:index_admin')}],
        }
        return render(request, 'admin/akun/login.html', data)

    def post(self, request):
        if not request.user.is_authenticated:
            email = request.POST.get('frm_email')
            pwd = request.POST.get('frm_pwd')

            is_email = check_is_email(email)
            
            if is_email:
                user = authenticate(request, email=email, password=pwd)
            else:
                try:
                    user = m_user.objects.get(username = email, is_active = True)
                    if not user.check_password(pwd):
                        user = None
                except Exception as e:
                    user = None
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Selamat datang {user.username} ({user.get_role_display().upper()})")
                print('masuk')
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    messages.success(request, f"Selamat datang {user.username} ({user.get_role_display().upper()})")
                    return redirect('app:index_dashboard')
            else:
                messages.error(request, "Login gagal, silahkan masukkan data dengan benar")
                return redirect('app:index_admin')
        else:
            return redirect('app:index_dashboard')


@method_decorator(login_required(), name='dispatch')
class LogoutViews(View):
    def get(self, request):
        logout_message = request.GET.get('logout_message', None)
        if logout_message is not None:
            messages.info(request, logout_message)
        
        logout(request)
        return redirect(request.META['HTTP_REFERER'])
        