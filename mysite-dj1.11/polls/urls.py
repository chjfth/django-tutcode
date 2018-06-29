from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


	# old: before tut04 generic view (ngv=non-generic view)
    # ex: /polls/ngv
    url(r'^$/ngv', views.index_ngv, name='index_ngv'),
    # ex: /polls/5/ngv
    url(r'^(?P<question_id>[0-9]+)/ngv$', views.detail_ngv, name='detail_ngv'),
    # ex: /polls/5/results/ngv
    url(r'^(?P<question_id>[0-9]+)/results/ngv$', views.results_ngv, name='results_ngv'),

	# old tut01 & tut02:
	url(r'^index0$', views.index0, name='index0'),
	url(r'^index1$', views.index1, name='index1'),
	url(r'^index_hardurl$', views.index_hardurl, name='index_hardurl'),
]
