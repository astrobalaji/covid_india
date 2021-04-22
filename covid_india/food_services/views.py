from django.shortcuts import render
from .models import food_ser
import json
# Create your views here.

code_state = json.load(open('lookup_data/code_state.json', 'r'))

def index(request, slug, *args, **kwargs):
    state_name = code_state[slug]
    obj = food_ser.objects.filter(State = slug)
    food_sup_lis = []
    for sup in obj.iterator():
        sup_context = {}
        sup_context['city'] = sup.City
        sup_context['area'] = sup.Area
        sup_context['name'] = sup.Name
        sup_context['number'] = sup.Number
        sup_context['hours'] = sup.Hours
        sup_context['service'] = sup.Service
        sup_context['social'] = sup.Social
        sup_context['delivery'] = sup.Delivery
        food_sup_lis.append(sup_context)
    if len(food_sup_lis) == 0:
        sup_exists = False
    else:
        sup_exists = True
    context = {}
    context['suppliers'] = food_sup_lis
    context['state_name'] = state_name
    context['state_code'] = slug
    context['sup_exists'] = sup_exists
    return render(request, 'food_sup.html', context)
