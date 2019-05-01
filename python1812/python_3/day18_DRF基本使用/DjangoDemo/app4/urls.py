from django.conf.urls import url

from app4 import views

urlpatterns = [
    url(r'^news/$', views.NewsAPIView.as_view()),
    url(r'^news/(?P<pk>[0-9]+)/$', views.NewsDetailAPIView.as_view()),
]