from django import forms
from rtlh_app.models import KontenPeraturan
from django.shortcuts import render, get_object_or_404

class KontenPeraturanForm(forms.ModelForm):  # APP
    class Meta:
        model = KontenPeraturan
        fields = ['judul', 'deskripsi', 'gambar']
