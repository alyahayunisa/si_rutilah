from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import kontak

class KontakViews(View):
    def get(self, request):
        data_kontak = kontak.objects.all()
        data = {
            'data_kontak' : data_kontak
        }
        return render(request, 'kontak/index.html', data)
       