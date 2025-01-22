from django.shortcuts import render, get_object_or_404
from rtlh_admin.models import undang_undang
from django.views import View


class TampilkanPeraturanViews(View):
    def get(self,request):
        data_undang = undang_undang.objects.all()
        data = {
            'data_undang' : data_undang
        }
        return render(request, 'beranda/index.html', data)