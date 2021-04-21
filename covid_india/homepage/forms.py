from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

states = [
            ('AP', 'Andhra Pradesh'),
            ('AR', 'Arunachal Pradesh'),
            ('AS', 'Assam'),
            ('BR', 'Bihar'),
            ('CG', 'Chhattisgarh'),
            ('GA', 'Goa'),
            ('GJ', 'Gujarat'),
            ('HR', 'Haryana'),
            ('HP', 'Himachal Pradesh'),
            ('JH', 'Jharkhand'),
            ('KA', 'Karnataka'),
            ('KL', 'Kerala'),
            ('MP', 'Madhya Pradesh'),
            ('MH', 'Maharashtra'),
            ('MN', 'Manipur'),
            ('ML', 'Meghalaya'),
            ('MZ', 'Mizoram'),
            ('NL', 'Nagaland'),
            ('OD', 'Odisha'),
            ('PB', 'Punjab'),
            ('RJ', 'Rajasthan'),
            ('SK', 'Sikkim'),
            ('TN', 'Tamil Nadu'),
            ('TS', 'Telangana'),
            ('TR', 'Tripura'),
            ('UP', 'Uttar Pradesh'),
            ('UK', 'Uttarakhand'),
            ('WB', 'West Bengal')
]
