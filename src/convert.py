import os
from dotenv import load_dotenv
import requests


load_dotenv()

token = os.getenv("API_KEY")


def transactions_convert(transactions: dict):
    """Конвертация валюты в RUB"""
    headers = {"apikey": token}
    amount = transactions["operationAmount"]["amount"]
    code = transactions["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    response = requests.get(url, headers=headers)
    return round(response.json().get("result"), 2)
    # return response.json()


# print(transactions_convert({"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
#                       "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#                       "description": "Перевод организации", "from": "Maestro 1596837868705199",
#                       "to": "Счет 64686473678894779589"}))
