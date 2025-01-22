from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import data_kriteria
from django.db import transaction
from django.contrib import messages
from django.urls import reverse

class KriteriaViews(View):
    def get(self, request):
        data_kri = data_kriteria.objects.all()
        # Ambil data kriteria untuk masing-masing tipe
        data_tipe_a = data_kriteria.objects.filter(kriteria="Tipe A").first()
        data_tipe_b = data_kriteria.objects.filter(kriteria="Tipe B").first()
        data_tipe_c = data_kriteria.objects.filter(kriteria="Tipe C").first()
        data_tipe_d = data_kriteria.objects.filter(kriteria="Tipe D").first()
        data_tipe_e = data_kriteria.objects.filter(kriteria="Tipe E").first()
        data_tipe_f = data_kriteria.objects.filter(kriteria="Tipe F").first()

        data = {
            'data_kri' : data_kri,
            'data_tipe_a': data_tipe_a,
            'data_tipe_b': data_tipe_b,
            'data_tipe_c': data_tipe_c,
            'data_tipe_d': data_tipe_d,
            'data_tipe_e': data_tipe_e,
            'data_tipe_f': data_tipe_f,
        }
        
        return render(request, 'kriteria/index.html', data)