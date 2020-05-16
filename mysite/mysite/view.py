from django.template.loader import render_to_string
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    renderer = render_to_string('current_datetime.html', {'current_date': now})
    return HttpResponse(renderer)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s</body></html>" %(offset, dt)
    return HttpResponse(html)
