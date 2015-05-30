from django.shortcuts import render
from django.views.generic import ListView
from organizations.models import Organization

class OrganizationsListView(ListView):
    queryset = Organization.objects.all()
    template_name = "organizations/list.html"

# Create your views here.
