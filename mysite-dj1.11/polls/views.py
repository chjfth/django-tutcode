from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

#
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/
#

from .models import Question

# plain-old index view from: 
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#write-views-that-actually-do-something
#
def index0(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)


# first template expansion example from:
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#write-views-that-actually-do-something
#
def index1(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))

# Using shortcut function: render()
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-render
#
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

#def detail(request, question_id):
#	return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
	# or simplify it with get_object_or_404()
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
   
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

