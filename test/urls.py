from django.conf.urls import patterns, include, url
from test import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # ex: /pbm/
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^hiring/$', views.HiringView.as_view(), name='hiring'),
    url(r'^all/$', views.AllView.as_view(), name='all'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^submitstartup/$', views.SubmitStartupView.as_view(), name='submitstartup'),
    url(r'^submitjob/$', views.SubmitJobView.as_view(), name='submitjob'),
    
    # Examples:
    # url(r'^$', 'test.views.home', name='home'),
    # url(r'^pbm/', include('test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
