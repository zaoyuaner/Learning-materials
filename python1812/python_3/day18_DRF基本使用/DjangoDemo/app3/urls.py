from django.conf.urls import url

from app3 import views

urlpatterns = [
    url(r'^book/$', views.BookAPIView.as_view()),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
]