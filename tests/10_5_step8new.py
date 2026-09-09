""" 
Банковские операции 
Напишите функцию bank(), имитирующую основные банковские операции: 
пополнение баланса, снятие наличных, оплату покупки и получение информации о балансе. 
Функция bank() принимает три аргумента в следующем порядке:

operation – строка, тип операции 
('top up' – пополнение, 'withdraw' – снятие наличных, 'pay' – оплата покупки, 
'show balance' – получение информации о балансе)

id – строка, содержащая уникальный идентификатор клиента

amount – целое число, сумма операции или значение None 
(для операции получения информации о балансе)

Функция bank() должна выполнить указанную операцию для клиента с соответствующим id. 
Для операции получения информации о балансе функция bank() должна вывести целое число. 
Изначально у каждого клиента баланс равен 0.

Примечание 1. 
Гарантируется, что не будет ситуации, когда оплата покупки или снятие наличных 
невозможны из-за нехватки средств на счете.

Примечание 2. Вызывать функцию bank() не нужно, требуется только реализовать ее.
"""

balances = {}


def bank(operation, id, amount):
    if id not in balances:
        balances[id] = 0

    if operation == 'top up':
        balances[id] += amount
    elif operation == 'withdraw':
        balances[id] -= amount
    elif operation == 'pay':
        balances[id] -= amount
    elif operation == 'show balance':
        print(balances[id])


arthur = 'id-1004'
tony = 'id-78923'
bank('top up', tony, 500)
bank('show balance', arthur, None)
bank('pay', tony, 120)
bank('top up', arthur, 1000)
bank('show balance', arthur, None)
bank('withdraw', tony, 200)
bank('show balance', tony, None)
