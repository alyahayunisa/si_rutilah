# Generated by Django 3.2.2 on 2025-01-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtlh_admin', '0004_undang_undang'),
    ]

    operations = [
        migrations.CreateModel(
            name='sekilas_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=300)),
                ('deskripsi', models.CharField(max_length=300, null=True)),
                ('img_info', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
