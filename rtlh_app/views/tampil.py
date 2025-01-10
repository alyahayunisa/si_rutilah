from django.shortcuts import render, get_object_or_404
from rtlh_app.models import KontenPeraturan
from django.views import View

class TampilkanPeraturanViews(View):
    def tampilkan_peraturan(request):
        konten = get_object_or_404(KontenPeraturan, id=1)  # Ambil konten pertama
        return render(request, 'peraturan.html', {'konten': konten})