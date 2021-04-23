from django.shortcuts import redirect, render
from .models import hosp_dat, hosp_city
from datetime import datetime
import json

code_state = json.load(open('lookup_data/code_state.json', 'r'))

# Create your views here.
def index(request, slug, *args, **kwargs):
    state_name = code_state[slug]
    if hosp_dat.objects.filter(state_code = slug).exists():
        obj = next(hosp_dat.objects.filter(state_code = slug).iterator())
        if obj.pointer == 'city':
            obj_city = hosp_city.objects.filter(state_code = slug).iterator()
            city_dat = []
            for city in obj_city:
                city_temp = {}
                city_temp['name'] = city.city
                city_temp['pointer'] = city.pointer
                city_dat.append(city_temp)
            context = {"cities":city_dat, "state_name":state_name}
            return render(request, "hosp_city_sel.html", context)
        else:
            return redirect(obj.pointer)
    else:
        return render(request, "hosp_not_avail.html")
