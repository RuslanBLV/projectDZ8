import json
from src.convert import transactions_convert
import logging
import os.path

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

file_name = "operations.json"
file_directory = "../data"
file_path = os.path.join(file_directory, file_name)


def financial_transactions(path: str):
    """Список всех транзакций"""
    logger.info(f"Ввод данных: {path}")
    try:
        with open(path, encoding="utf-8") as transactions:
            try:
                logger.info("Форматирование в тип 'list'")
                data = json.load(transactions)
                filtered_data = [item for item in data if item]
                if isinstance(filtered_data, list):
                    logger.info(f"Результат {data}")
                    return filtered_data
                else:
                    logger.error("В файле нет списка")
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


result_list = financial_transactions(file_path)
# if isinstance(result_list, list):
#     print(result_list)
# else:
#     print("das")

def amount_transactions(trans: list):
    """Вывод 'amount' и условие надо ли отправлять запрос на конвертацию"""
    logger.info(f"Ввод данных: {trans}")
    for transactions in trans:
        logger.info("Обработка валюты")
        if transactions["operationAmount"]["currency"]["code"] == "RUB":
            logger.info("Валюта RUB")
            result = transactions["operationAmount"]["amount"]
            logger.info(f"Результат {result}")
            return result
        else:
            logger.info("Конвертация валюты в RUB")
            amount = transactions_convert(transactions)
            logger.info(f"Результат {amount}")
            return amount

# print(result_list)
# print(amount_transactions(result))
# amount_transactions([{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
#                       "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#                       "description": "Перевод организации", "from": "Maestro 1596837868705199",
#                       "to": "Счет 64686473678894779589"}])
# print(financial_transactions("../data/operations.json"))
