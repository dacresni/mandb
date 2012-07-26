from django.shortcuts import render_to_response , redirect
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
import logging

#logger = logging.getLogger(django.request)


def by_name(request ):
    name = request.POST['name']
    return redirect("/static/mantext/%s.txt"%name)
