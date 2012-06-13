from django.shortcuts import render_to_response
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

#def index(request):
#    return 

def by_name(request, name):
    try:
        return direct_to_template(request, template="templates/mantext/%s.txt"% name)
    except TemplateDoesNotExist:
        raise Http404()

