import imp
from django.http import HttpResponse


def index(requst):
    return HttpResponse('Hello Docker')