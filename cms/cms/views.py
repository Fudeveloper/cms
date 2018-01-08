from django.shortcuts import render

# Create your views here.

from django.conf import settings

import logging

logging.getLogger('cms.views')


def innerIndex(request):
    return render(request, 'innerIndex.html')


def refuse(request):
    return render(request, 'refuse.html')
