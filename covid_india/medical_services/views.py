from django.shortcuts import render
import pandas as pd
from .models import med_serv
from covid_india import settings
from sqlalchemy import create_engine
from django.db import transaction
import json

code_state = json.load(open('lookup_data/code_state.json', 'r'))
# Create your views here.
#@transaction.commit_manually
def update_from_csv():
    df = pd.read_csv("../data/Remedesivir_cleaned.csv")
    for item in df.to_dict('records'):
        entry = med_serv(**item)
        entry.save()
    transaction.commit()

def index(request, slug, *args, **kwargs):
    state = code_state[slug]
    obj = med_serv.objects.filter(state_code = slug)
    med_sup_lis = []
    for sup in obj.iterator():
        sup_context = {}
        sup_context['dist_name'] = sup.dist_name
        sup_context['telephone'] = sup.telephone
        sup_context['address'] = sup.address
        sup_context['email'] = sup.email
        med_sup_lis.append(sup_context)
    if len(med_sup_lis) == 0:
        sup_exists = False
    else:
        sup_exists = True
    context = {}
    context['suppliers'] = med_sup_lis
    context['state_name'] = state
    context['sup_exists'] = sup_exists
    return render(request, 'rem_sup.html', context)
