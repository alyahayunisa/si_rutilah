# Generated by Django 3.2.2 on 2025-01-09 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtlh_admin', '0013_auto_20250109_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='kriteriartlh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=300)),
                ('deskripsi', models.CharField(max_length=300, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons/')),
            ],
        ),
        migrations.AddField(
            model_name='tips',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/'),
        ),
    ]
