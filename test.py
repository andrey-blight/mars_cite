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
    print(post('http://localhost:8080/api/v2/users', json={'surname': 'Surname'}).json())  # Некоректный зап
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

    # Получение
    print(get('http://localhost:8080/api/v2/users').json())  # Получение всех пользователей


def user_tests():
    # получение
    print(get('http://localhost:8080/api/v2/users/1').json())  # Получение первого пользователя
    print(get('http://localhost:8080/api/v2/users/3').json())  # Получение третьего пользователя
    print(get('http://localhost:8080/api/v2/users/300').json())  # Ошибка индекса
    print(get('http://localhost:8080/api/v2/users/dfe').json())  # Ошибка строка в индексе

    # print(post('http://localhost:8080/api/jobs', json={'job': 'Заголовок'}).json())  # Некоректный запрос
    #

    # print(post('http://localhost:8080/api/jobs',
    #            json={'id': 5,
    #                  'team_leader': 1,
    #                  'job': 'Title',
    #                  'work_size': 1,
    #                  'collaborators': "1,2,3,4,5",
    #                  'is_finished': False}).json())  # Корректный запрос
    # print(get('http://localhost:8080/api/jobs').json())  # Получение всех работ


def delete_test():
    print(delete('http://localhost:8080/api/jobs/100').json())  # ошибка индекса
    print(delete('http://localhost:8080/api/jobs/1').json())  # Корректный запрос
    print(get('http://localhost:8080/api/jobs').json())  # Получение всех работ


def change_test():
    print(put('http://localhost:8080/api/jobs/100').json())  # ошибка индекса
    print(put('http://localhost:8080/api/jobs/1').json())  # Пустой запрос
    print(put('http://localhost:8080/api/jobs/1', json={'job': 'Заголовок'}).json())  # Некоректный запрос
    print(put('http://localhost:8080/api/jobs/1',
              json={'id': 1,
                    'team_leader': 1,
                    'job': 'Title',
                    'work_size': 1,
                    'collaborators': "1,2,3,4,5",
                    'is_finished': False}).json())  # Корректный запрос
    print(get('http://localhost:8080/api/jobs/1').json())  # Получение всех работ


if __name__ == '__main__':
    list_users_test()
