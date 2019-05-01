from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^wheel/$', views.WheelAPIView.as_view()),
    url(r'^wheel/(?P<pk>\d+)/$', views.WheelDetail.as_view()),
]