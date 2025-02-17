# Generated by Django 3.2.2 on 2025-01-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtlh_admin', '0016_auto_20250115_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_kriteria',
            name='img_kriteria',
            field=models.ImageField(null=True, upload_to='kriteria/'),
        ),
        migrations.AlterField(
            model_name='data_rtlh',
            name='img_rumah',
            field=models.ImageField(null=True, upload_to='rumah/'),
        ),
        migrations.AlterField(
            model_name='permohonan',
            name='img_kk',
            field=models.ImageField(null=True, upload_to='kk/'),
        ),
        migrations.AlterField(
            model_name='permohonan',
            name='img_ktp',
            field=models.ImageField(null=True, upload_to='ktp/'),
        ),
        migrations.AlterField(
            model_name='permohonan',
            name='img_rumah',
            field=models.ImageField(null=True, upload_to='rumah/'),
        ),
        migrations.AlterField(
            model_name='permohonan',
            name='img_sertifikat',
            field=models.ImageField(null=True, upload_to='sertifikat/'),
        ),
        migrations.AlterField(
            model_name='sekilas_info',
            name='img_info',
            field=models.ImageField(null=True, upload_to='info/'),
        ),
        migrations.AlterField(
            model_name='undang_undang',
            name='img_uu',
            field=models.ImageField(null=True, upload_to='uu/'),
        ),
    ]
