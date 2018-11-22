from django.shortcuts import render
from django.contrib.auth import models
from django.http import HttpResponse
from django.template import RequestContext, Template
from django.utils import timezone
from .models import Plato
from .forms import PlatoForm
# Create your views here.
def nuevo_plato(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        
    else:
        form = PlatoForm()
    return render(request, 'restaurant/nuevo_plato.html', {'form': form})
