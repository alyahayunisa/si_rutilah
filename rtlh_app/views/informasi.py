from django.shortcuts import render, redirect
from django.views import View

class InformasiViews(View):
    def get(self, request):
        return render(request, 'informasi/index.html')
    
       
