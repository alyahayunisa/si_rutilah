from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import uuid, os
from datetime import datetime
from django.utils.text import slugify
import random, string
#from taggit.managers import TaggableManager
#from django.utils.translation import ugettext_lazy as _

class data_kriteria(models.Model):
    kriteria = models.CharField(max_length=300)
    desk_singkat = models.CharField(max_length=300)
    desk_detail = models.CharField(max_length=300)
    desk_full = models.CharField(max_length=500, null=True)
    img_tipe = models.ImageField(null=True, upload_to='tipe/')

    def __str__(self):
        return self.kriteria


class data_rumah(models.Model):
    no_kk = models.CharField(null=True, max_length=20)
    nik = models.CharField(null=True, max_length=20)
    nama_kk = models.CharField(max_length=300)
    pendidikan = models.CharField(null=True, max_length=300)
    jenis_kelamin = models.CharField(null=True, max_length=300)
    tempat_lahir = models.CharField(null=True, max_length=100)
    tanggal_lahir = models.DateField(null=True)
    agama = models.CharField(max_length=300)
    alamat_lengkap = models.CharField(null=True, max_length=300)
    kelurahan = models.CharField(null=True, max_length=300)
    jumlah_anggota = models.CharField(null=True, max_length=300)
    no_hp = models.CharField(null=True, max_length=20)
    pekerjaan = models.CharField(null=True, max_length=300)
    penghasilan = models.CharField(null=True, max_length=300)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Data Rumah {self.nama_kk}"

class permohonan(models.Model):
    nama_kk = models.ForeignKey(data_rumah, on_delete=models.CASCADE, related_name="permohonan")
    img_ktp = models.ImageField(null=True, upload_to='ktp/')
    img_kk = models.ImageField(null=True, upload_to='kk/')
    img_rumah = models.ImageField(null=True, upload_to='rumah/')
    img_sertifikat = models.ImageField(null=True, upload_to='sertifikat/')

    def __str__(self):
        return f"Permohonan dari {self.nama_kk.nama_kk}"

class data_rtlh(models.Model):
    nama_kk = models.ForeignKey(data_rumah, on_delete=models.CASCADE, related_name="rtlh")
    status_tanah = models.CharField(max_length=300)
    status_kepemilikan = models.CharField(max_length=300)
    luas_tanah = models.CharField(max_length=300)
    status_rumah = models.CharField(max_length=300)
    luas_bangunan = models.CharField(max_length=300)
    kondisi_pondasi = models.CharField(max_length=300)
    kondisi_atap = models.CharField(max_length=300)
    kondisi_lantai = models.CharField(max_length=300)
    kondisi_dinding = models.CharField(max_length=300)
    kondisi_ventilasi = models.CharField(max_length=300)
    kondisi_toilet = models.CharField(max_length=300)
    sumber_airbersih = models.CharField(max_length=300)
    sumber_listrik = models.CharField(max_length=300)
    kriteria = models.ForeignKey(data_kriteria, on_delete=models.SET_NULL, null=True, related_name='rtlh_kriteria')
    img_rumah = models.ImageField(null=True, upload_to='rumah/')
    tgl_input = models.DateField(null=True)

    def __str__(self):
        return f"Data RTLH {self.nama_kk.nama_kk}"

class verifikasi(models.Model):
    nama_kk = models.ForeignKey(data_rumah, on_delete=models.CASCADE, related_name="verifikasi")
    tanggal_verifikasi = models.DateField(null=True)
    status_pengajuan = models.CharField(null=True, max_length=300)
    alasan = models.CharField(null=True, max_length=300)

    def __str__(self):
        return f"Verifikasi {self.nama_kk.nama_kk}"

class informasi(models.Model):
    judul = models.CharField(max_length=300)
    deskripsi = models.CharField(null=True, max_length=300)
    img_informasi = models.ImageField(null=True, upload_to='informasi/')

    def __str__(self):
        return self.judul


ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('posting', 'Posting'),
]

ACCESS_CHOICES = [
    ('public', 'Public'),
    ('private', 'Private'),
]



class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, phone, password, **extra_fields):
        values = [email, username, phone,]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, phone, password, **extra_fields)

    def create_superuser(self, email, username, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_verified') is not True:
            raise ValueError('Superuser must have is_verified=True.')

        return self._create_user(email, username, phone, password, **extra_fields)
    
class Master_User(AbstractBaseUser):
    user_id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)
    # avatar = models.ImageField(blank=True, null=True, upload_to='images/avatar/')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='posting')
    email_verification_token = models.CharField(max_length=100, default='')
    
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'role', 'is_superuser']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name


class undang_undang(models.Model):
    judul = models.CharField(max_length=300)
    deskripsi = models.CharField(null=True, max_length=300)
    img_uu = models.ImageField(null=True, upload_to='uu/')

    def __str__(self):
        return self.judul
    
class sekilas_info(models.Model):
    judul = models.CharField(max_length=300)
    deskripsi = models.CharField(null=True, max_length=300)
    img_info = models.ImageField(null=True, upload_to='info/')

    def __str__(self):
        return self.judul

class tips(models.Model):
    judul = models.CharField(max_length=300)
    deskripsi = models.CharField(null=True, max_length=300)
    icon = models.ImageField(upload_to='icons_tips/', null=True, blank=True)  # Field baru

    def __str__(self):
        return self.judul
    
class kontak(models.Model):
    alamat = models.CharField(max_length=300)
    no_hp = models.CharField(null=True, max_length=20)
    latitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=9, decimal_places=6)

    def __str__(self):
        return self.alamat
    
class kriteriartlh(models.Model):
    judul = models.CharField(max_length=300)
    deskripsi = models.CharField(null=True, max_length=300)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)  # Field baru

    def __str__(self):
        return self.judul
