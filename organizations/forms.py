from django.forms import ModelForm
from organizations.models import Organization
from django_countries.widgets import CountrySelectWidget

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'country', 'city']
        widgets = {
            'country': CountrySelectWidget()
        }
