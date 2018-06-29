from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/
#

from django.template import loader

from .models import Question

# plain-old index view from: 
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#write-views-that-actually-do-something
def index0(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# first template expansion example from:
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#write-views-that-actually-do-something
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))


def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

