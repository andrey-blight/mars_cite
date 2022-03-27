from requests import *


def list_users_test():
    # Получение
    print(get('http://localhost:8080/api/v2/users').json())  # Получение всех пользователей

    # Добавление
    print(post('http://localhost:8080/api/v2/users').json())  # Пустой запрос
    print(post('http://localhost:8080/api/v2/users',
               json={'id': 1,
                     'surname': "Ivanov",
                     'name': 'Andrey',
                     'age': 25,
                     'position': "Driver",
                     'speciality': "driver rover",
                     'address': "module 5",
                     'email': "i_a@mail.ru",
                     'city_from': "San Hose"}).json())  # Ошибка существующего id
    print(post('http://localhost:8080/api/v2/users', json={'surname': 'Surname'}).json())  # Некоректный запрос
    print(post('http://localhost:8080/api/v2/users',
               json={'id': 10,
                     'surname': "Ivanov",
                     'name': 'Andrey',
                     'age': 25,
                     'position': "Driver",
                     'speciality': "driver rover",
                     'address': "module 5",
                     'email': "i_a@mail.ru",
                     'city_from': "San Hose"}).json())  # Корректный запрос
    print(get('http://localhost:8080/api/v2/users').json())  # Получение всех пользователей


def user_tests():
    # получение
    print(get('http://localhost:8080/api/v2/users/1').json())  # Получение первого пользователя
    print(get('http://localhost:8080/api/v2/users/3').json())  # Получение третьего пользователя
    print(get('http://localhost:8080/api/v2/users/300').json())  # Ошибка индекса
    print(get('http://localhost:8080/api/v2/users/dfe').json())  # Ошибка строка в индексе

    # удаление
    print(delete('http://localhost:8080/api/v2/users/100').json())  # ошибка индекса
    print(delete('http://localhost:8080/api/v2/users/fgrie').json())  # несуществующий адресс
    print(delete('http://localhost:8080/api/v2/users/1').json())  # Корректный запрос
    print(get('http://localhost:8080/api/v2/users').json())  # Получение всех пользователей

    # изменение
    print(put('http://localhost:8080/api/v2/users/1').json())  # Пустой запрос
    print(put('http://localhost:8080/api/v2/users/100').json())  # Несуществующий id
    print(put('http://localhost:8080/api/v2/users/1',
              json={'id': 2,
                    'surname': "Ivanov",
                    'name': 'Andrey',
                    'age': 25,
                    'position': "Driver",
                    'speciality': "driver rover",
                    'address': "module 5",
                    'email': "i_a@mail.ru",
                    'city_from': "San Hose"}).json())  # Ошибка существующего id
    print(put('http://localhost:8080/api/v2/users/1', json={'surname': 'Surname'}).json())  # Некоректный запрос
    print(put('http://localhost:8080/api/v2/users/1',
              json={'id': 10,
                    'surname': "Ivanov",
                    'name': 'Andrey',
                    'age': 25,
                    'position': "Driver",
                    'speciality': "driver rover",
                    'address': "module 5",
                    'email': "i_a@mail.ru",
                    'city_from': "San Hose"}).json())  # Корректный запрос
    print(get('http://localhost:8080/api/v2/users').json())  # Получение всех пользователей


def list_jobs_test():
    # Получение
    print(get('http://localhost:8080/api/v2/jobs').json())  # Получение всех работ

    # Добавление
    print(post('http://localhost:8080/api/v2/jobs').json())  # Пустой запрос
    print(post('http://localhost:8080/api/v2/jobs',
               json={'id': 1,
                     'team_leader': 2,
                     'job': 'First_job',
                     'work_size': 25,
                     'collaborators': "1, 2, 3, 4",
                     'is_finished': False, }).json())  # Ошибка существующего id
    print(post('http://localhost:8080/api/v2/jobs',
               json={'id': 10,
                     'team_leader': 105,
                     'job': 'First_job',
                     'work_size': 25,
                     'collaborators': "1, 2, 3, 4",
                     'is_finished': False, }).json())  # Не существующий team leader
    print(post('http://localhost:8080/api/v2/jobs', json={'job': 'First_job'}).json())  # Некоректный запрос
    print(post('http://localhost:8080/api/v2/jobs',
               json={'id': 10,
                     'team_leader': 2,
                     'job': 'First_job',
                     'work_size': 25,
                     'collaborators': "1, 2, 3, 4",
                     'is_finished': False, }).json())  # Корректный запрос
    print(get('http://localhost:8080/api/v2/jobs').json())  # Получение всех работ


if __name__ == '__main__':
    # list_users_test()
    # user_tests()
    # list_jobs_test()
