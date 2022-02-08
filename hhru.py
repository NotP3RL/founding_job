from itertools import count

import requests

from tools import predict_salary


def get_hh_vacancies(languages):
    vacancies = {}

    for language in languages:
        sum_salary = 0
        vacancies_processed = 0
        for page_number in count(0, 1):
            params = {
                'specialization': '1.221',
                'area': '1',
                'period': '30',
                'per_page': '100',
                'page': page_number,
                'text': language
            }
            response = requests.get('https://api.hh.ru/vacancies', params=params)
            response.raise_for_status()
            for vacancy in response.json()['items']:
                if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
                    sum_salary += predict_salary(
                        vacancy['salary']['from'],
                        vacancy['salary']['to']
                    )
                    vacancies_processed += 1
            if page_number >= response.json()['pages'] - 1:
                break
        vacancies[language] = {
            'vacancies_found': response.json()['found'],
            'vacancies_processed': vacancies_processed,
            'average_salary': int(sum_salary / vacancies_processed)
        }
    return vacancies
