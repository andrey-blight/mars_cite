from requests import *


def get_test():
    print(get('http://localhost:8080/api/jobs').json())  # Получение всех работ
    one = get('http://localhost:8080/api/jobs/1').json()  # Одна работа без ошибок
    if 'error' not in one:
        print("Одна работа без ошибок")
    one = get('http://localhost:8080/api/jobs/999').json()  # Одна работа с ошибками
    if 'error' in one:
        print("Ошибка : Неверный индекс")
    one = get('http://localhost:8080/api/jobs/йццц').json()  # Одна работа с ошибками
    if 'error' in one:
        print("Ошибка : Текст а не идекс")


def create_test():
    print(post('http://localhost:8080/api/jobs').json())  # пустой запрос

    print(post('http://localhost:8080/api/jobs', json={'job': 'Заголовок'}).json())  # Некоректный запрос

    print(post('http://localhost:8080/api/jobs',
               json={'id': 1,
                     'team_leader': 1,
                     'job': 'Title',
                     'work_size': 1,
                     'collaborators': "1,2,3,4,5",
                     'is_finished': False}).json())  # Ошибка id Корректный запрос
    print(post('http://localhost:8080/api/jobs',
               json={'id': 5,
                     'team_leader': 1,
                     'job': 'Title',
                     'work_size': 1,
                     'collaborators': "1,2,3,4,5",
                     'is_finished': False}).json())  # Корректный запрос
    print(get('http://localhost:8080/api/jobs').json())  # Получение всех работ


if __name__ == '__main__':
    create_test()
