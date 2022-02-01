from itertools import count
from math import ceil

import requests

from tools import predict_salary


def get_sj_vacancies(languages, token):
    headers = {
        'X-Api-App-Id': token
    }
    vacancies = {

    }
    vacancy_count_per_page = 100
    for language in languages:
        sum_salary = 0
        vacancies_processed = 0
        for page_number in count(0,1):
            params = {
                'town': 'Moscow',
                'catalogues': '48',
                'keyword': language,
                'count': vacancy_count_per_page,
                'page': page_number
            }
            response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers = headers, params = params)
            response.raise_for_status()
            for vacancy in response.json()['objects']:
                if vacancy['currency'] == 'rub':
                    sum_salary += predict_salary(vacancy['payment_from'], vacancy['payment_to'])
                    vacancies_processed += 1
            if page_number >= ceil(response.json()['total'] / vacancy_count_per_page) - 1:
                break
        vacancies[language] = {
        'vacancies_found': response.json()['total'],
        'vacancies_processed': vacancies_processed,
        'average_salary': int(sum_salary / vacancies_processed)
        }
    return vacancies
