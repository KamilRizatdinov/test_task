from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from api.serializers import SubjectSerializer
from app.models import Subject
from app.utils import fetch_data, get_subject_by_query_string


# Create your views here.
@csrf_exempt
def subjects_list(request):
    if request.method == 'GET':
        subjects= Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        query_string = request.POST.get('query', '')
        subject = get_subject_by_query_string(query_string=query_string)

        if subject and subject.requested_recently():
            subject.request_time = timezone.now()
            subject.save(update_fields=['request_time'])
            serializer = SubjectSerializer(data=subject.to_dict())
            if serializer.is_valid():
                return JsonResponse(serializer.data, status=201)
        else:
            data = fetch_data(
                url='https://rmsp.nalog.ru/search-proc.json',
                query_string=query_string,
            )
            if data:
                subject = Subject(**data)
                subject.save()
                subject.query_set.create(query_string=query_string)
                serializer = SubjectSerializer(data=subject.to_dict())
                if serializer.is_valid():
                    return JsonResponse(serializer.data, status=201)

        return JsonResponse({'error': 'Query string is invalid'}, status=400)
