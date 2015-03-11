from django.conf.urls import patterns, include, url
from django.contrib import admin
class nodo:
    def __init__(self):
        print "nuevo objeto"

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Servidor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    jose = nodo()
)