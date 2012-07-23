from django.shortcuts import render_to_response
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.base import TemplateView

#def index(request):
#    return 

def by_name(request, name):
    try:
        return TemplateView.as_view(template_name="/app/static/mantext/%s.txt"% name)
    except TemplateDoesNotExist:
        raise Http404()

