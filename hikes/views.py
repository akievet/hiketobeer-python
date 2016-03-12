from django.shortcuts import render
from hikes.models import Hike

def home_page(request):
    return render(request, 'home.html')

def view_hike(request, hike_id):
    hike = Hike.objects.get(id=hike_id)
    return render(request, 'hike.html', {'hike': hike})
