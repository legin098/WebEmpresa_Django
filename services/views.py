from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
  return render(request, 'services/services.html', {'services': Service.objects.all()})