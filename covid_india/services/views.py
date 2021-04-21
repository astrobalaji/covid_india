from django.shortcuts import render

# Create your views here.

def index(request, slug, *args, **kwargs):
    return render(request, 'page2.html')
