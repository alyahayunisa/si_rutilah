from django.urls import path, include, re_path
from .views import *
from django.conf.urls.static import static

app_name = 'rtlh_admin'

urlpatterns = [
    path('login/', auth.LoginViews.as_view(), name = 'login'),
    path('dashboard/', dashboard.DashboardViews.as_view(), name = 'dashboard'),
    path('formrmh/', formrmh.FormRmhViews.as_view(), name = 'formrmh'),
    path('register/', register.RegisterViews.as_view(), name = 'register'),
    path('profile/', profile.ProfileViews.as_view(), name = 'profile'),
    path('edit/<int:id_dashboard>', dashboard.EditDaftarViews.as_view(), name = 'edit'),
    path('delete/<int:id_dashboard>', dashboard.DeleteDaftarViews.as_view(), name = 'delete'),
    path('kriteria/', kriteria.KriteriaViews.as_view(), name = 'kriteria'),
    path('user/', user.UserViews.as_view(), name = 'user'),
    path('ket/', ket.KetViews.as_view(), name = 'keterangan'),
    path('buang/<int:id_kriteria>', kriteria.HapusKriteriaViews.as_view(), name = 'buang'),
    path('create/', kriteria.CreateKriteriaViews.as_view(), name = 'create'),
    path('editkri/<int:id_kriteria>', kriteria.EditKriteriaViews.as_view(), name = 'editkri'),
    path('bantuan/', bantuan.BantuanViews.as_view(), name = 'bantuan'),
    path('hapus/', user.HapusUserViews.as_view(), name = 'hapususer'),
    path('hps/<int:id_keterangan>', ket.HapusKetViews.as_view(), name = 'hps'),
    path('tambah/', ket.TambahViews.as_view(), name = 'tambahket'),
    path('tambahbantuan/', bantuan.TambahBantuanViews.as_view(), name = 'tambahbantuan'),
    path('ubahbantu/<int:id_bantuan>', bantuan.UbahBantuanViews.as_view(), name = 'ubahbantu'),
    path('del/<int:id_bantuan>', bantuan.DelBantuanViews.as_view(), name = 'delbantu'),
    path('tambahrtlh/', rtlh.TambahRtlhViews.as_view(), name = 'tambahrtlh'),
    path('rtlh/', rtlh.RtlhViews.as_view(), name = 'rtlh'),
    path('ubahrtlh/<int:id_rtlh>', rtlh.UbahRtlhViews.as_view(), name = 'ubahrtlh'),
    path('hapusrtlh/<int:id_rtlh>', rtlh.HapusRtlhViews.as_view(), name = 'hapusrtlh'),
    path('verif/', verif.VerifViews.as_view(), name = 'verifikasi'),
    path('tambahverif/', verif.TambahVerifViews.as_view(), name = 'tambahverif'),
    path('ubahverif/<int:id_verif>', verif.UbahVerifViews.as_view(), name = 'ubahverif'),
    path('hpsverif/<int:id_verif>', verif.HapusVerifViews.as_view(), name = 'hpsverif'),
    path('info/', info.InformasiViews.as_view(), name = 'informasi'),
    path('tambahinfo/', info.TambahInfoViews.as_view(), name = 'tambahinfo'),
    path('editinfo/<int:id_info>', info.EditInfoViews.as_view(), name = 'editinfo'),
    path('hapusinfo/<int:id_info>', info.HapusInfoViews.as_view(), name = 'hapusinfo'),
   

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)