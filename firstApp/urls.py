
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^firstApp/', views.index, name='index'),
]
"""

from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^firstApp/', include('firstApp.urls')),
]
"""