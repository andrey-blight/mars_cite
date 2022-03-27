from requests import *


def list_users_test():
    print(get('http://localhost:8080/api/v2/users').json())  # Получение всех пользователей


def user_tests():
    print(get('http://localhost:8080/api/v2/users/1').json())  # Получение первого пользователя
    print(get('http://localhost:8080/api/v2/users/3').json())  # Получение третьего пользователя
    print(get('http://localhost:8080/api/v2/users/300').json())  # Ошибка индекса
    print(get('http://localhost:8080/api/v2/users/dfe').json())  # Ошибка строка в индексе
    # print(post('http://localhost:8080/api/jobs', json={'job': 'Заголовок'}).json())  # Некоректный запрос
    #
    # print(post('http://localhost:8080/api/jobs',
    #            json={'id': 1,
    #                  'team_leader': 1,
    #                  'job': 'Title',
    #                  'work_size': 1,
    #                  'collaborators': "1,2,3,4,5",
    #                  'is_finished': False}).json())  # Ошибка id
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
    user_tests()
