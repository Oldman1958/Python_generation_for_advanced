""" 
Строка запроса
Query String (строка запроса) – часть URL с передаваемыми на сервер параметрами 
в виде пары ключ — значение, которые разделены символом равно = 
и указываются после вопросительного знака ?. 
Если параметров несколько, то они разделяются амперсандом &.

Например:

в URL-адресе https://pygen.ru?page=1 строкой запроса является page=1
в URL-адресе https://pygen.ru?page=1&per=5&sort=True 
строкой запроса является page=1&per=5&sort=True
Напишите функцию add_query_string(), которая принимает два аргумента в следующем порядке:

url – строка с URL-адресом
query – словарь с параметрами
Функция должна возвращать URL-адрес, содержащий строку запроса, сформированную из этих параметров.

Примечание. Вызывать функцию add_query_string() не нужно, требуется только реализовать ее.
"""


def add_query_string(url, query={}):
    if len(query) == 0:
        return url
    result_url = f'{url}?'
    for k, v in query.items():
        result_url += f'&{k}={query[k]}'
    return result_url


print(add_query_string('pygen.ru', {'per': '10', 'page': 1}))
print(add_query_string('pygen.ru', {}))
print(add_query_string('pygen.ru', {'page': 1}))
print(
    add_query_string(
        'pygen.ru', {'page': 1, 'sort': True, 'rank': 'top'}
    )
)
