import json
from typing import Any

from src.convert import transactions_convert


def financial_transactions(path: str):
    """ Список всех транзакций """
    try:
        with open(path, encoding='utf-8') as transactions:
            try:
                data = json.load(transactions)
            except json.JSONDecodeError:
                print("ощибка обработки файла")
                return []
        return data
    except FileNotFoundError:
        print("Файл не найден")
        return []


result = financial_transactions('../data/operations.json')


def amount_transactions(trans: list):
    for transactions in trans:
        amount = transactions_convert(transactions)
        return amount


# amount_transactions([{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
#                       "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#                       "description": "Перевод организации", "from": "Maestro 1596837868705199",
#                       "to": "Счет 64686473678894779589"}])
