from django.forms import ModelForm
from breaks.models import Break

class BreakForm(ModelForm):
    class Meta:
        model = Break
        fields = ['description', 'office', 'duration', 'start_time']
