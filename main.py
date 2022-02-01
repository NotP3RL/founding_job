import os

from dotenv import load_dotenv

from hhru import get_hh_vacancies
from superjob import get_sj_vacancies
from tools import get_vacancy_table

LANGUAGES = [
    'JavaScript',
    'Java',
    'Python',
    'Ruby',
    'PHP',
    'C++',
    'C#',
    'C'
]

if __name__ == '__main__':
    load_dotenv()
    superjob_token = os.getenv('SUPERJOB_TOKEN')
    print(get_vacancy_table(get_hh_vacancies(LANGUAGES), 'HeadHunter'))
    print(get_vacancy_table(get_sj_vacancies(LANGUAGES, superjob_token), 'SuperJob'))
