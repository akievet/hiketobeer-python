from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def view_hike(request, hike_id):
    return render(request, 'hike.html')
