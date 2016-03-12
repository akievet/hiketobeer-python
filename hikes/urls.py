from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hikes import views

urlpatterns = [
    url(r'^(\d+)/', views.view_hike, name='view_hike')
]

urlpatterns += staticfiles_urlpatterns()
