from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string
from rtlh_admin.models import data_rtlh
from django.urls import reverse
#from django.http import JsonResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from datetime import datetime
from django.utils.dateparse import parse_date

class LaporanViews(View):
    def get(self, request):
         # Ambil query parameter untuk filter tanggal
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        
        # Query data
        data_rumahrtlh = data_rtlh.objects.all()

        # Filter berdasarkan periode tanggal jika parameter diberikan
        if start_date:
            start_date = parse_date(start_date)
            if start_date:
                data_rumahrtlh = data_rumahrtlh.filter(tgl_input__gte=start_date)
        
        if end_date:
            end_date = parse_date(end_date)
            if end_date:
                data_rumahrtlh = data_rumahrtlh.filter(tgl_input__lte=end_date)
        
        # Data untuk template
        data = {
            'data_rumahrtlh': data_rumahrtlh,
            'filters': {
                'start_date': start_date,
                'end_date': end_date,
            }
        }

        # Check if the request is for PDF export
        if request.GET.get('export') == 'pdf':
            return self.export_to_pdf(data)

        return render(request, 'admin/laporan/index.html', data)
    
    

    def export_to_pdf(self, context):
        template_path = 'admin/laporan/pdf.html'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Laporan_RTLH.pdf"'

        # Render the template with context
        template = get_template(template_path)
        html = template.render(context)

        # Convert HTML to PDF
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('Error generating PDF', status=500)
        return response
    
    