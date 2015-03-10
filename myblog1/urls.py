from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
import blog.urls
import sysadmin.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^blog', include(blog.urls)),
    url(r'^sysadmin', include(sysadmin.urls)),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'manage_login.html'}),
)