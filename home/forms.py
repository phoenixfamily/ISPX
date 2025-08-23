from django import forms
from .models import CooperationRequest


class CooperationForm(forms.Form):
    ac_type  = forms.CharField(max_length=100)
    date     = forms.DateField(input_formats=["%Y-%m-%d"])
    ac_reg   = forms.CharField(max_length=100)

    station  = forms.CharField(max_length=100, required=False)
    time     = forms.TimeField(input_formats=["%H:%M"], required=False)
    customer = forms.CharField(max_length=200, required=False)

    task_cabin    = forms.BooleanField(required=False)
    task_exterior = forms.BooleanField(required=False)

    def clean_ac_type(self):
        v = self.cleaned_data["ac_type"].strip()
        if not v:
            raise forms.ValidationError("This field is required.")
        return v

    def clean_ac_reg(self):
        v = self.cleaned_data["ac_reg"].strip()
        if not v:
            raise forms.ValidationError("This field is required.")
        return v

    def clean_station(self):
        v = self.cleaned_data.get("station", "")
        return v.strip()

    def clean_customer(self):
        v = self.cleaned_data.get("customer", "")
        return v.strip()
