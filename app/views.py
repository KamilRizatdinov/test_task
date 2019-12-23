from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request=request, template_name='app/index.html', context={})


def query(request):
    return HttpResponseRedirect(reverse('app:index'))
