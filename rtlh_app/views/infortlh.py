from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import informasi


class InformasiViews(View):
    def get(self, request):
        data_info = informasi.objects.all()
        data = {
            'data_info' : data_info
        }
        return render(request, 'informasi/index.html',data)
       
    
       
