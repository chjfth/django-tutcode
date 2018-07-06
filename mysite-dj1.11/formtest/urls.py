from django.conf.urls import url

from . import views

app_name = 'formtest'

urlpatterns = [
    # ex: mtform/
    # i.e. multipartform demo from http://www.evernote.com/l/ABWzLd-1TV1AJITW40vAPQVl4scVpTL7apE/
    url(r'^$', views.mtform, name='mtform'),
]
