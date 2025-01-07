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

class KontenPeraturan(models.Model):
    judul = models.CharField(max_length=255, verbose_name="Judul")
    deskripsi = models.TextField(verbose_name="Deskripsi")
    gambar = models.ImageField(upload_to='uploads/peraturan/', verbose_name="Gambar", blank=True, null=True)

    def __str__(self):
        return self.judul