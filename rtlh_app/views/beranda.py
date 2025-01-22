from django.shortcuts import render, redirect
from django.views import View
from rtlh_admin.models import undang_undang, sekilas_info, kriteriartlh, tips, data_rumah
from rtlh_admin.models import permohonan,verifikasi, data_rtlh

class BerandaViews(View):
    def get(self,request):
        data_undang = undang_undang.objects.all()
        data_sekilas = sekilas_info.objects.all()
        data_krirtlh = kriteriartlh.objects.all()
        data_tips = tips.objects.all()
        total_pemilik = data_rumah.objects.count()
        total_permohonan = permohonan.objects.count()
        total_verifikasi = verifikasi.objects.count()
        total_RTLH = data_rtlh.objects.count()
        total_proses = verifikasi.objects.filter(status_pengajuan='Proses').count()
        total_ditolak = verifikasi.objects.filter(status_pengajuan='Ditolak').count()
        total_disetujui = verifikasi.objects.filter(status_pengajuan='Disetujui').count()
        data = {
            'data_undang' : data_undang,
            'data_sekilas' : data_sekilas,
            'data_krirtlh': data_krirtlh,
            'data_tips': data_tips,
            'total_pemilik': total_pemilik,
            'total_permohonan': total_permohonan,
            'total_verifikasi': total_verifikasi,
            'total_RTLH': total_RTLH,
            'total_proses': total_proses,
            'total_ditolak': total_ditolak,
            'total_disetujui': total_disetujui,
        }
        return render(request, 'beranda/index.html', data)
    
       