from django.shortcuts import render
from whatsapp_groups.models import whatsapp_groups
import json
# Create your views here.
code_state = json.load(open('lookup_data/code_state.json', 'r'))
def index(request, slug, *args, **kwargs):
    state = code_state[slug]
    if whatsapp_groups.objects.filter(state_code = slug).exists():
        wa_obj = next(whatsapp_groups.objects.filter(state_code = slug).iterator())
        wa_url = wa_obj.group_url
        wa_exists = True
    else:
        wa_exists = False
        wa_url = ''
    return render(request, 'services.html', {'state_name':state, 'state_code':slug, 'wa_url':wa_url, 'wa_exists':wa_exists})
