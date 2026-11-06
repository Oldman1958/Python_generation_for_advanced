""" 
Функция ignore_command() принимает на вход один строковый аргумент command – команда, 
которую нужно проверить, и возвращает значение True, если в команде содержится подстрока из списка ignore, 
или False – если нет.

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True

    return False

                  
Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any(), сохранив при этом ее функционал.

Примечание. Вызывать функцию ignore_command() не нужно, требуется только реализовать ее.
"""


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    result = any(map(lambda x: True if x in ignore else False, ignore))
    return result


print(ignore_command('get ip'))
