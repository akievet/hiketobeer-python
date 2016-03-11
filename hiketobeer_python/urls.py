from django.conf.urls import include, url
from hikes import views as hike_views
from hikes import urls as hike_urls

urlpatterns = [
    url(r'^$', hike_views.home_page, name='home'),
    url(r'^hikes/', include(hike_urls)),
    # url(r'^admin/', include(admin.site.urls)),
]
