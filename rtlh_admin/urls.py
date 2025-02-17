from django.urls import path, include, re_path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'rtlh_admin'

urlpatterns = [
    path('', auth.LoginViews.as_view(), name = 'login'),
    path('dashboard/', dashboard.DashboardViews.as_view(), name = 'dashboard'),
    path('formrmh/', formrmh.FormRmhViews.as_view(), name = 'formrmh'),
    path('profile/', profile.ProfileViews.as_view(), name = 'profile'),
    path('edit/<int:id_dashboard>', dashboard.EditDaftarViews.as_view(), name = 'edit'),
    path('delete/<int:id_dashboard>', dashboard.DeleteDaftarViews.as_view(), name = 'delete'),
    path('kriteria/', kriteria.KriteriaViews.as_view(), name = 'kriteria'),
    path('user/', user.UserViews.as_view(), name = 'user'),
    path('buang/<int:id_kriteria>', kriteria.HapusKriteriaViews.as_view(), name = 'buang'),
    path('create/', kriteria.CreateKriteriaViews.as_view(), name = 'create'),
    path('editkri/<int:id_kriteria>', kriteria.EditKriteriaViews.as_view(), name = 'edit_kri'),
    path('bantuan/', bantuan.BantuanViews.as_view(), name = 'bantuan'),
    path('deleteuser/', user.HapusUserViews.as_view(), name = 'deleteuser'),
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
    path('logout/', auth.LogoutViews.as_view(), name = 'logout'),
    path('tambahuser/', user.TambahUserViews.as_view(), name = 'tambahuser'),
    path('undang/', undang.UndangViews.as_view(), name = 'undang'),
    path('tambahuu/', undang.TambahUndangViews.as_view(), name = 'tambah_uu'),
    path('ubahuu/<int:id_undang>', undang.EditUndangViews.as_view(), name = 'ubah_uu'),
    path('hpsuu/<int:id_undang>', undang.HapusUndangViews.as_view(), name = 'hps_uu'),
    path('sekilas/', sekilas.SekilasInfoViews.as_view(), name = 'sekilas'),
    path('tambahsekilas/', sekilas.TambahSekilasViews.as_view(), name = 'tambah_sekilas'),
    path('ubahsekilas/<int:id_sekilas>', sekilas.EditSekilasViews.as_view(), name = 'ubah_sekilas'),
    path('hpssekilas/<int:id_sekilas>', sekilas.HapusSekilasViews.as_view(), name = 'hps_sekilas'),
    path('tipsrtlh/', tipsrtlh.TipsrtlhViews.as_view(), name = 'tips'),
    path('tambahtips/', tipsrtlh.TambahTipsrtlhViews.as_view(), name = 'tambah_tips'),
    path('ubahtips/<int:id_tipsrtlh>', tipsrtlh.EditTipsrtlhViews.as_view(), name = 'ubah_tips'),
    path('hpstips/<int:id_tipsrtlh>', tipsrtlh.HapusTipsrtlhViews.as_view(), name = 'hps_tips'),
    path('kontakhub/', kontakhub.KontakhubViews.as_view(), name = 'kontak'),
    path('tambahkontak/', kontakhub.TambahKontakhubViews.as_view(), name = 'tambah_kontak'),
    path('ubahkontak/<int:id_kontakhub>', kontakhub.EditKontakhubViews.as_view(), name = 'ubah_kontak'),
    path('hpskontak/<int:id_kontakhub>', kontakhub.HapusKontakhubViews.as_view(), name = 'hps_kontak'),
    path('krirtlh/', krirtlh.FnKrirtlhViews.as_view(), name = 'kriteriartlh'),
    path('tambahkri/', krirtlh.TambahKrirtlhViews.as_view(), name = 'tambah_kri'),
    path('ubahkri/<int:id_krirtlh>', krirtlh.EditKrirtlhViews.as_view(), name = 'ubah_kri'),
    path('hpskri/<int:id_krirtlh>', krirtlh.HapusKrirtlhViews.as_view(), name = 'hps_kri'),
    path('laporan/', laporan.LaporanViews.as_view(), name = 'laporan'),
    #path('periode/', laporan.LaporanPeriodeViews.as_view(), name = 'periode'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)