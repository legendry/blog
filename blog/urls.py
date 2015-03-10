from django.conf.urls import patterns,url
from blog import views

urlpatterns = patterns(
    url(r'^$',views.index),
    url(r'/detail/(?P<blogid>\d+)/$', views.detail),
    url(r'/search/', views.search),
    url(r'/searchbycategory', views.searchbycategory),
)
