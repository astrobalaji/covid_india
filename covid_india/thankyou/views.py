from django.shortcuts import render
from volunteer_ob.models import VolunteerOB
# Create your views here.

def index(request, pk, *args, **kwargs):
    vol_data = next(VolunteerOB.objects.filter(pk=pk).iterator())
    context = {"vol_name":vol_data.name}
    return render(request, 'Thankyou.html', context)
