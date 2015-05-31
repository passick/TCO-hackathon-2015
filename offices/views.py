from django.shortcuts import render
from offices.models import Office
from django.views.generic import TemplateView, ListView

class OfficeListView(ListView):
    model = Office
    template_name = "offices/list.html"

class OfficeView(TemplateView):
    template_name = "offices/info.html"

    def get_context_data(self, **kwargs):
        context = super(OfficeView, self).get_context_data(**kwargs)
        context['office'] = Office.objects.get(pk=kwargs['pk'])
        return context
    
# Create your views here.
