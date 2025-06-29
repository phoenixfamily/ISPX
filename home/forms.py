from django import forms
from .models import CooperationRequest

class CooperationRequestForm(forms.ModelForm):
    class Meta:
        model = CooperationRequest
        fields = [
            'ac_type', 'date', 'ac_reg', 'station', 'time', 'customer',
            'task_cabin', 'task_exterior'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
