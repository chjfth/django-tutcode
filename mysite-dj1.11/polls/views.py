from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect # tut04
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls  import reverse # tut04
from django.views import generic # tut04

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
def index_hardurl(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index_hardurl.html', context)

# Improvement: Removing hardcoded URLs in templates
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#removing-hardcoded-urls-in-templates
#
def index_ngv(request): # tut04: non-generic view
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)



#def detail(request, question_id):
#	return HttpResponse("You're looking at question %s." % question_id)

def detail_ngv(request, question_id): # tut04: non-generic view
	# or simplify it with get_object_or_404()
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
   
	return render(request, 'polls/detail.html', {'question': question})

def results_ngv(request, question_id): # tut04: non-generic view
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})


# Use generic views 
# https://docs.djangoproject.com/en/1.11/intro/tutorial04/#use-generic-views-less-code-is-better
#
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



# Processing a real vote form:
# https://docs.djangoproject.com/en/1.11/intro/tutorial04/
#
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(
			request, 
			'polls/detail.html', 
			{
				'question': question,
				'error_message': "You didn't select a choice.",
			}
		)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#

