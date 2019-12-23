from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json 
import requests
from app.models import Subject
from api.serializers import SubjectSerializer


# Create your views here.
@csrf_exempt
def subjects_list(request):
    if request.method == 'GET':
        snippets = Subject.objects.all()
        serializer = SubjectSerializer(snippets, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        # endpoint = "https://rmsp.nalog.ru/search-proc.json"
        data = JSONParser().parse(request)
        # r = requests.post(url=endpoint,
        #                   data={'query': query_string, 'mode': 'quick'})
        # json_data = json.loads(r.text)['data']
        # serializer = SubjectSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        return JsonResponse(data, status=201)
    # return JsonResponse(serializer.errors, status=400)
