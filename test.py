from requests import *

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
