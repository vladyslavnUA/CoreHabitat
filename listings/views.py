from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'templates/base.html'
    return render(request, template_name)

# Create your views here.
