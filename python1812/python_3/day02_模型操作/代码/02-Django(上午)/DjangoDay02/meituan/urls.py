from django.conf.urls import url

from meituan import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cart/$', views.cart),

    url(r'^addstu/$', views.addstu),
    url(r'^changestu/$', views.changestu),
]