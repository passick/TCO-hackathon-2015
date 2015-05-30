from django.forms import ModelForm
from offices.models import Office

class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = ['name', 'organization']
