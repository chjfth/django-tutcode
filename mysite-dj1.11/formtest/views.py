from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect # tut04
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls  import reverse # tut04

# Create your views here.

def mtform(request):
	
	return render(request, 'formtest/mtform.html')
