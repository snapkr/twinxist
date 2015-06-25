from django.conf.urls import url

from account import views

urlpatterns = [
    url(r'^inloggen', views.inloggen, name='inloggen'),
    url(r'^uitloggen', views.uitloggen, name='uitloggen'),
]