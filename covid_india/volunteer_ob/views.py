from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import VolOb
from .models import VolunteerOB
import json

code_state = json.load(open('lookup_data/code_state.json', 'r'))

# Create your views here.
class VolObViews(View):
    form_class = VolOb

    def get(self, request):
        form = self.form_class()
        return render(request, 'Volunteer_reg.html', {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            volOBdata = form.save(commit = False)
            volOBdata.state = code_state[volOBdata.state_code]
            volOBdata.save()
            return redirect('/thankyou/'+str(volOBdata.pk))
