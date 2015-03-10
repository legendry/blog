from django.conf.urls import patterns,url
from sysadmin import views

urlpatterns = patterns(
    url(r'^$',views.manage_blog),
    url(r'/blog',views.manage_blog),
    url(r'/login', views.manage_login),
    url(r'/logout', views.manage_logout),
    url(r'/addcategory',views.addcategory),
    url(r'/addblog',views.addblog),
    url(r'/updateblog', views.updateblog),
    url(r'/blog', views.manage_blog),
    url(r'/search', views.search),
    url(r'/searchbycategory', views.searchbycategory),
)
