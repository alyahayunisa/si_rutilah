from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import data_kriteria

class DetailKriteriaViews(View):
    def get(self, request):
        data_kri = data_kriteria.objects.all()
        data_tipe_b = data_kriteria.objects.filter(kriteria="Tipe B").first()
        data = {
            'data_kri' : data_kri,
            #'data_tipe_a': data_tipe_a,
            'data_tipe_b': data_tipe_b,
            #'data_tipe_c': data_tipe_c,
            #'data_tipe_d': data_tipe_d,
            #'data_tipe_e': data_tipe_e,
            #'data_tipe_f': data_tipe_f,
        }
        return render(request, 'kriteria/detailB.html', data)
    