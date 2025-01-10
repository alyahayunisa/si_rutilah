from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import *
from django.db import transaction
from django.contrib import messages
from django.urls import reverse
from rtlh_app.forms import KontenPeraturanForm
from rtlh_app.models import KontenPeraturan

class UbahPeraturanViews(View):
    def ubah_peraturan(request):  # ADMIN
        konten = KontenPeraturan.objects.first()  # Mengambil data pertama dari database
        if request.method == 'POST':
            form = KontenPeraturanForm(request.POST, request.FILES, instance=konten)
            if form.is_valid():
                form.save()
                messages.success(request, "Konten berhasil diperbarui.")
                return redirect('tampilkan_peraturan')  # Arahkan ke halaman publik
            else:
                messages.error(request, "Terjadi kesalahan. Silakan periksa kembali.")
        else:
            form = KontenPeraturanForm(instance=konten)
        return render(request, 'admin/ubah_peraturan.html', {'form': form})