from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import state_sel
# Create your views here.
def index(request):
    return render(request, 'index.html')

class home_view(View):
    form_class = state_sel

    def get(self, request):
        form = self.form_class()
        return render(request, "index.html", {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            states = form.data
            return redirect('/services/'+states.get('state'))
