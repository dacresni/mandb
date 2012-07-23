from django.shortcuts import render_to_response
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
import logging

logger = logging.getLogger(__name__)


def by_name(request ):
    try:
        return direct_to_template(request, template="/app/static/mantext/%s.txt"%request.POST['name'])
    except TemplateDoesNotExist:
        raise Http404()

