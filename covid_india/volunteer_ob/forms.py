from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import VolunteerOB
import json

state_choices = [
            ('AN', 'Andaman and Nicobar Islands'),
            ('AP', 'Andhra Pradesh'),
            ('AR', 'Arunachal Pradesh'),
            ('AS', 'Assam'),
            ('BR', 'Bihar'),
            ('CH', 'Chandigarh'),
            ('CG', 'Chhattisgarh'),
            ('DD', 'Dadra and Nagar Haveli and Daman and Diu'),
            ('DL', 'Delhi'),
            ('GA', 'Goa'),
            ('GJ', 'Gujarat'),
            ('HR', 'Haryana'),
            ('HP', 'Himachal Pradesh'),
            ('JK', 'Jammu and Kashmir'),
            ('JH', 'Jharkhand'),
            ('KA', 'Karnataka'),
            ('KL', 'Kerala'),
            ('LA', 'Ladakh'),
            ('LD', 'Lakshadweep'),
            ('MP', 'Madhya Pradesh'),
            ('MH', 'Maharashtra'),
            ('MN', 'Manipur'),
            ('ML', 'Meghalaya'),
            ('MZ', 'Mizoram'),
            ('NL', 'Nagaland'),
            ('OD', 'Odisha'),
            ('PB', 'Punjab'),
            ('PY', 'Puducherry'),
            ('RJ', 'Rajasthan'),
            ('SK', 'Sikkim'),
            ('TN', 'Tamil Nadu'),
            ('TS', 'Telangana'),
            ('TR', 'Tripura'),
            ('UP', 'Uttar Pradesh'),
            ('UK', 'Uttarakhand'),
            ('WB', 'West Bengal'),
]

class VolOb(forms.ModelForm):
    name = forms.CharField(label = 'Name', required = True, widget = forms.TextInput(attrs={'style': 'width: 100%', 'cols': 200,'rows': 1}))
    city = forms.CharField(label = 'City', required = True, widget = forms.TextInput(attrs={'style': 'width: 100%', 'cols': 200,'rows': 1}))
    state_code = forms.ChoiceField(label = 'State',choices = state_choices, required = True,widget=forms.Select(attrs={'style': 'width: 100%', 'cols': 200,'rows': 1}))
    number = forms.CharField(label = 'Mobile Number', required = True, widget = forms.TextInput(attrs={'style': 'width: 100%', 'cols': 200,'rows': 1}))
    email = forms.CharField(label = 'Email Address', required = True, widget = forms.TextInput(attrs={'style': 'width: 100%', 'cols': 200,'rows': 1}))
    services_offered = forms.CharField(widget = forms.Textarea(attrs={'style': 'width: 100%'}), label = 'Services offered', help_text = "Separate each one of them by a comma (',')", required = True)

    class Meta:
        model = VolunteerOB
        exclude = ['state']
    def clean(self):
        cleaned_data = super().clean()
        number_check = cleaned_data.get('number')
        if not number_check.isnumeric():
            raise forms.ValidationError("Please enter only numeric values. Avoid special characters like '+', '-', '/',etc.")
        return cleaned_data
