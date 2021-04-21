from django.shortcuts import render
import json
# Create your views here.
code_state = json.load(open('lookup_data/code_state.json', 'r'))
def index(request, slug, *args, **kwargs):
    state = code_state[slug]
    return render(request, 'services.html', {'state_name':state, 'state_code':slug})
