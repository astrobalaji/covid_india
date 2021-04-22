from django.shortcuts import render
from volunteer_ob.models import VolunteerOB
import json
# Create your views here.

code_state = json.load(open('lookup_data/code_state.json', 'r'))

def index(request, slug, *args, **kwargs):
    state = code_state[slug]
    obj = VolunteerOB.objects.filter(state_code = slug)
    Volunteers_lis = []
    for vol in obj.iterator():
        vol_context = {}
        vol_context['volunteer_name'] = vol.name
        vol_context['number'] = vol.number
        vol_context['city'] = vol.city
        vol_context['services'] = vol.services_offered
        Volunteers_lis.append(vol_context)
    if len(Volunteers_lis) == 0:
        vol_exists = False
    else:
        vol_exists = True
    context = {}
    context['volunteers'] = Volunteers_lis
    context['state_name'] = state
    context['vol_exists'] = vol_exists
    return render(request, 'volunteer_list.html', context)
