from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^login/', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/', logout, {'template_name': 'accounts/logout.html'}),
]
