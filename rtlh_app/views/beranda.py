from django.shortcuts import render, redirect
from django.views import View

class BerandaViews(View):
    def get(self,request):
        return render(request, 'beranda/index.html')
    
       