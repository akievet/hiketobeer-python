from django.conf.urls import url
from hikes import views

urlpatterns = [
    url(r'^(\d+)/', views.view_hike, name='view_hike')
]
