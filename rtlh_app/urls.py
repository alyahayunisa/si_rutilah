
from django.urls import path, include, re_path
from .views import *
from django.conf.urls.static import static

app_name = 'rtlh_app'


urlpatterns = [
    path('beranda/', beranda.BerandaViews.as_view(), name = 'beranda'),
    path('berita/', berita.BeritaViews.as_view(), name = 'berita'),
    path('kriteria/', kriteria.KriteriaViews.as_view(), name = 'kriteria'),
    path('kontak/', kontak.KontakViews.as_view(), name = 'kontak'),
    path('daftar/', daftar.DaftarViews.as_view(), name = 'daftar'),
    path('informasi/', informasi.InformasiViews.as_view(), name = 'informasi'),
    path('kriteria_A/', kriteria_A.DetailKriteriaViews.as_view(), name = 'detailA'),
    path('kriteria_B/', kriteria_B.DetailKriteriaViews.as_view(), name = 'detailB'),
    path('kriteria_C/', kriteria_C.DetailKriteriaViews.as_view(), name = 'detailC'),
    path('kriteria_D/', kriteria_D.DetailKriteriaViews.as_view(), name = 'detailD'),
    path('kriteria_E/', kriteria_E.DetailKriteriaViews.as_view(), name = 'detailE'),
    path('kriteria_F/', kriteria_F.DetailKriteriaViews.as_view(), name = 'detailF'),
] 

