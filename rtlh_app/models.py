from django.db import models

class daftar_rumah(models.Model):
    nama_pemilik = models.CharField(max_length=300)
    keterangan = models.CharField(max_length=300)
    kriteria = models.CharField(max_length=300)

class data_rumah(models.Model):
    no_kk = models.IntegerField(null=True, default=0)
    nik = models.IntegerField(null=True, default=0)
    nama_kk = models.CharField(max_length=300)
    alamat = models.CharField(max_length=300)
    pekerjaan = models.CharField(max_length=300)
    keterangan = models.CharField(max_length=300)
    kriteria = models.CharField(max_length=300)
    status_pengajuan = models.CharField(max_length=300)