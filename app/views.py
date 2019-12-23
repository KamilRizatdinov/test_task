import json

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
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


def all(request):
    try:
        subjects_list = Subject.objects.all().order_by('-request_time')
    except IndexError:
        subjects_list = None

    return render(request=request,
                  template_name='app/all.html',
                  context={'subjects_list': subjects_list})


def query(request):
    endpoint = "https://rmsp.nalog.ru/search-proc.json"
    query_string = request.POST['query']
    r = requests.post(url=endpoint, data={'query': query_string, 'mode': 'quick'})
    json_data = json.loads(r.text)['data']

    if r.status_code != 200 or not json_data:
        return HttpResponseRedirect(reverse('app:index'))
    else:
        data = json_data[0]
        subject = Subject(
            inn=data['inn'],
            request_time=timezone.now(),
            ogrn=data['ogrn'],
            cityname=data['cityname'],
            citytype=data['citytype'],
            registration_date=data['dtregistry'],
            name_ex=data['name_ex'],
            description=data['okved1name']
        )
        subject.save()

    return HttpResponseRedirect(reverse('app:index'))

