from django.shortcuts import render, redirect
from django.views import View

class DetailKriteriaViews(View):
    def get(self, request):
        return render(request, 'kriteria/detailF.html')
    