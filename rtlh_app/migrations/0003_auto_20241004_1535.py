# Generated by Django 3.2 on 2024-10-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtlh_app', '0002_detail_daftar'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_rumah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_kk', models.IntegerField(default=0, null=True)),
                ('nik', models.IntegerField(default=0, null=True)),
                ('nama_kk', models.CharField(max_length=300)),
                ('alamat', models.CharField(max_length=300)),
                ('pekerjaan', models.CharField(max_length=300)),
                ('keterangan', models.CharField(max_length=300)),
                ('kriteria', models.CharField(max_length=300)),
                ('status_pengajuan', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='detail_daftar',
        ),
    ]