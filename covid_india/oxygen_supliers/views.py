from django.shortcuts import render
from .models import oxy_sup
import json

code_state = json.load(open('lookup_data/code_state.json', 'r'))
# Create your views here.
def index(request, slug, *args, **kwargs):
    state_name = code_state[slug]
    objs = oxy_sup.objects.filter(state_code = slug).iterator()
    sup_lis = []
    for oxy in objs:
        sup_temp = {}
        sup_temp['Contact'] = oxy.Contact
        sup_temp['Number'] = oxy.Number
        sup_temp['City'] = oxy.City
        sup_lis.append(sup_temp)
    if len(sup_lis) != 0:
        sup_exists = True
    else:
        sup_exists = False
    context = {'state_name':state_name, 'sup_lis':sup_lis, 'sup_exists':sup_exists}
    return render(request, 'oxy_sup.html', context)
