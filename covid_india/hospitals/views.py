from django.shortcuts import redirect, render
from .models import hosp_dat
from datetime import datetime

# Create your views here.
def index(request, slug, *args, **kwargs):
    if hosp_dat.objects.filter(state_code = slug).exists():
        obj = next(hosp_dat.objects.filter(state_code = slug).iterator())
        if slug == 'WB':
            day = datetime.today().date().day - 1
            month = datetime.today().date().month
            pointer = obj.pointer.replace('date_month', str(day)+'.'+str(month))
        return redirect(obj.pointer)
    else:
        return render(request, "hosp_not_avail.html")
