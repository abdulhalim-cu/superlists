from django.conf.urls import include, url
from lists import views as list_views
from lists import urls as list_urls
from django.contrib import admin

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^lists/', include(list_urls)),
]
