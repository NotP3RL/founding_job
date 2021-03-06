from terminaltables import AsciiTable


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_to:
        return salary_to * 0.8
    elif salary_from:
        return salary_from * 1.2


def get_vacancy_table(vacancies, title):
    table_data = [
        ['Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        ]
    ]
    for language, info in vacancies.items():
        table_data.append([
                language,
                info['vacancies_found'],
                info['vacancies_processed'],
                info['average_salary']]
            )
    return AsciiTable(table_data, title).table
