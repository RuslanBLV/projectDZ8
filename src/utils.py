import json
from typing import Any
from src.convert import transactions_convert
import logging


logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def financial_transactions(path: str):
    """ Список всех транзакций """
    logger.info(f"Ввод данных: {path}")
    try:
        with open(path, encoding='utf-8') as transactions:
            try:
                logger.info(f"Форматирование в тип 'list'")
                data = json.load(transactions)
                if type(data) == list:
                    logger.info(f"Результат {data}")
                    return data
                else:
                    logger.error(f"В файле нет списка")
                    print("В файле нет списка")
                    return []
            except json.JSONDecodeError as error:
                logger.error(f"ощибка {error}")
                print("ощибка обработки файла")
                return []
    except FileNotFoundError as error_2:
        logger.error(f"ощибка {error_2}")
        print("Файл не найден")
        return []


result = financial_transactions('../data/operations.json')


def amount_transactions(trans: list):
    """Вывод 'amount' и условие надо ли отправлять запрос на конвертацию"""
    logger.info(f"Ввод данных: {trans}")
    for transactions in trans:
        logger.info(f"Обработка валюты")
        if transactions['operationAmount']['currency']['code'] == "RUB":
            logger.info(f"Валюта RUB")
            result = transactions['operationAmount']['amount']
            logger.info(f"Результат {result}")
            return result
        else:
            logger.info(f"Конвертация валюты в RUB")
            amount = transactions_convert(transactions)
            logger.info(f"Результат {amount}")
            return amount

# print(result)
# print(amount_transactions(result))
# amount_transactions([{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
#                       "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#                       "description": "Перевод организации", "from": "Maestro 1596837868705199",
#                       "to": "Счет 64686473678894779589"}])
