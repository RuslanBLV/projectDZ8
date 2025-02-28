import json
from typing import Any
from src.convert import transactions_convert


def financial_transactions(path: str):
    """ Список всех транзакций """
    try:
        with open(path, encoding='utf-8') as transactions:
            try:
                data = json.load(transactions)
                if type(data) == list:
                    return data
                else:
                    print("В файле нет списка")
                    return []
            except json.JSONDecodeError:
                print("ощибка обработки файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


result = financial_transactions('../data/operations.json')


def amount_transactions(trans: list):
    """Вывод 'amount' и условие надо ли отправлять запрос на конвертацию"""
    for transactions in trans:
        if transactions['operationAmount']['currency']['code'] == "RUB":
            return transactions['operationAmount']['amount']
        else:
            amount = transactions_convert(transactions)
            return amount

# print(result)
# print(amount_transactions(result))
# amount_transactions([{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
#                       "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#                       "description": "Перевод организации", "from": "Maestro 1596837868705199",
#                       "to": "Счет 64686473678894779589"}])
