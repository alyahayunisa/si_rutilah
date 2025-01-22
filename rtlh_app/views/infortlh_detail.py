from django.shortcuts import render, get_object_or_404
from django.views import View
from rtlh_admin.models import informasi

class InfoDetailViews(View):
    model = informasi
    template_name = 'detail_informasi.html'
    context_object_name = 'info'

    def get(self, request, id_info):
        data_info = informasi.objects.all()
        data_info = get_object_or_404(informasi, id=id_info)
        data = {
            'info': data_info
        }
        return render(request, 'informasi/infodetail.html', data)
    
