from django.shortcuts import render, redirect
from django.views import View

class RegisterViews(View):
    def get(self, request):
        return render(request, 'admin/akun/register.html')