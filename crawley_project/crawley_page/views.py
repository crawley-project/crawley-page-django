# Create your views here.

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import Context, Template, RequestContext

def index(req):
        
    return render_to_response("index.html")

def about(req):
    
    return render_to_response("about.html")

