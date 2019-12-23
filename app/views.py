import json

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
import requests

from app.models import Subject


# Create your views here.
def index(request):
    try:
        subject = Subject.objects.all().order_by('-request_time')[0]
    except IndexError:
        subject = None

    return render(request=request,
                  template_name='app/index.html',
                  context={'subject': subject})


def query(request):
    endpoint = "https://rmsp.nalog.ru/search-proc.json"
    query_string = request.POST['query']
    r = requests.post(url=endpoint, data={'query': query_string, 'mode': 'quick'})
    json_data = json.loads(r.text)['data']

    if r.status_code != 200 or not json_data:
        return HttpResponseRedirect(reverse('app:index'))
    else:
        subject = Subject(query_string=query_string, result=json_data[0]['name_ex'])
        subject.save()

    return HttpResponseRedirect(reverse('app:index'))

