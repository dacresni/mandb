from django.shortcuts import render_to_response
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
import logging

#logger = logging.getLogger(django.request)


def by_name(request ):
    name = request.POST['name']
    try:
        return direct_to_template(request, template= u'static/mantext/%s.txt'%name)
    except TemplateDoesNotExist:
        raise Http404("post: %s"%str(request.POST))

