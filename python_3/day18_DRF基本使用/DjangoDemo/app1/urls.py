from django.conf.urls import url

from app1 import views

urlpatterns = [
    url(r'^wheels/$', views.wheels, name='wheels'),

    url(r'^hello/$', views.HelloView.as_view())
]