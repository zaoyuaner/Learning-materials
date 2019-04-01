from django.conf.urls import url

from app3 import views

urlpatterns = {
    url(r'^user/$', views.UserAPIView.as_view()),

    url(r'^addr/$', views.AddrAPIView.as_view({
        'get': 'list',
        'post': 'create',
    })),
    url(r'^addr/(?P<pk>\d+)/$', views.AddrAPIView.as_view({
        'get': 'retrieve',
        'patch': 'partial_update'
    })),
}