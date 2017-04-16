# Create your views here.

from django.http import HttpResponse


def login(req):
    return HttpResponse("<a>hello</a>")
