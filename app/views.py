from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils import timezone

from app.models import Subject
from app.utils import fetch_data, get_subject_by_query_string


# Create your views here.
def index(request):
    try:
        subject = Subject.objects.latest('request_time')
    except IndexError:
        subject = None

    return render(request=request,
                  template_name='app/index.html',
                  context={'subject': subject})


def show_all(request):
    try:
        subjects_list = Subject.objects.all().order_by('-request_time')
    except IndexError:
        subjects_list = None

    return render(request=request,
                  template_name='app/all.html',
                  context={'subjects_list': subjects_list})


def query(request):
    query_string = request.POST.get('query', '')
    subject = get_subject_by_query_string(query_string=query_string)

    if subject and subject.requested_recently():
        subject.request_time = timezone.now()
        subject.save(update_fields=['request_time'])
    else:
        data = fetch_data(
            url='https://rmsp.nalog.ru/search-proc.json',
            query_string=query_string,
        )
        if data:
            subject = Subject(**data)
            subject.save()
            subject.query_set.create(query_string=query_string)

    return HttpResponseRedirect(reverse('app:index'))
