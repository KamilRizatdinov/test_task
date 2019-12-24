import json

import requests
from django.utils import timezone

from app.models import Query


def fetch_data(url='', query_string=''):
    r = requests.post(url=url,
                      data={'query': query_string, 'mode': 'quick'})
    if r.status_code == 200:
        data_list = json.loads(r.text)['data']
        if data_list:
            data_dict = data_list[0]
            data = {
                'inn': data_dict['inn'],
                'ogrn': data_dict['ogrn'],
                'name_ex': data_dict['name_ex'],
                'registration_date': data_dict['dtregistry'],
                'request_time': timezone.now()
            }

            return data


def get_subject_by_query_string(query_string):
    try:
        return Query.objects.get(query_string=query_string).result
    except Query.DoesNotExist:
        return None
