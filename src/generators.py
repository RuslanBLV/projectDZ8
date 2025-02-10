transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

transactions_clear = str([])


def filter_by_currency(transactions: list, currency: str):
    """Выводит транзакции по запросу валюты"""
    error = "Список пуст"
    if transactions == "[]":
        yield error
        return
    elif len(transactions) != 0:
        if currency == "USD" or currency == "RUB":
            for i in transactions:
                if i["operationAmount"]["currency"]["code"] == currency:
                    yield i
        elif currency != "USD" and currency != "RUB":
            yield "Нет такой валюты"
            return


def transaction_descriptions(transactions: list):
    """Выводит какая операция была произведена"""
    if transactions == "[]":
        yield "Список пуст"
        return
    limit = 0
    for i in transactions:
        limit += 1
        yield i["description"]
    if limit == len(transactions):
        while True:
            yield "Список закончился"


def card_number_generator(range_start: int, range_stop: int):
    """генерирует номер карт"""
    range_stop += 1
    if range_stop > 10000000000000001 or range_start > 10000000000000001:
        yield "Неверный лимит"
        return
    range_list = range(range_start, range_stop)
    generator = [x for x in range_list]
    result_list = []
    for i in generator:
        if i < 10:
            result = f"0000 0000 0000 000{i}"
            result_list.append(result)
        elif 100 > i >= 10:
            result = f"0000 0000 0000 00{i}"
            result_list.append(result)
        elif 1000 > i >= 100:
            result = f"0000 0000 0000 0{i}"
            result_list.append(result)
        elif 10000 > i >= 1000:
            result = f"0000 0000 0000 {i}"
            result_list.append(result)
        elif 100000 > i >= 10000:
            i_srt = str(i)
            result = f"0000 0000 000{i_srt[0]} {i_srt[1:5]}"
            result_list.append(result)
        elif 1000000 > i >= 100000:
            i_srt = str(i)
            result = f"0000 0000 00{i_srt[0:2]} {i_srt[2:6]}"
            result_list.append(result)
        elif 10000000 > i >= 1000000:
            i_srt = str(i)
            result = f"0000 0000 0{i_srt[0:3]} {i_srt[3:7]}"
            result_list.append(result)
        elif 100000000 > i >= 10000000:
            i_srt = str(i)
            result = f"0000 0000 {i_srt[0:4]} {i_srt[4:8]}"
            result_list.append(result)
        elif 1000000000 > i >= 100000000:
            i_srt = str(i)
            result = f"0000 000{i_srt[0]} {i_srt[1:5]} {i_srt[5:9]}"
            result_list.append(result)
        elif 10000000000 > i >= 1000000000:
            i_srt = str(i)
            result = f"0000 00{i_srt[0:2]} {i_srt[2:6]} {i_srt[6:10]}"
            result_list.append(result)
        elif 100000000000 > i >= 10000000000:
            i_srt = str(i)
            result = f"0000 0{i_srt[0:3]} {i_srt[3:7]} {i_srt[7:11]}"
            result_list.append(result)
        elif 1000000000000 > i >= 100000000000:
            i_srt = str(i)
            result = f"0000 {i_srt[0:4]} {i_srt[4:8]} {i_srt[8:12]}"
            result_list.append(result)
        elif 10000000000000 > i >= 1000000000000:
            i_srt = str(i)
            result = f"000{i_srt[0]} {i_srt[1:5]} {i_srt[5:9]} {i_srt[9:13]}"
            result_list.append(result)
        elif 100000000000000 > i >= 10000000000000:
            i_srt = str(i)
            result = f"00{i_srt[0:2]} {i_srt[2:6]} {i_srt[6:10]} {i_srt[10:14]}"
            result_list.append(result)
        elif 1000000000000000 > i >= 100000000000000:
            i_srt = str(i)
            result = f"0{i_srt[0:3]} {i_srt[3:7]} {i_srt[7:11]} {i_srt[11:15]}"
            result_list.append(result)
        elif 10000000000000000 > i >= 1000000000000000:
            i_srt = str(i)
            result = f"{i_srt[0:4]} {i_srt[4:8]} {i_srt[8:12]} {i_srt[12:16]}"
            result_list.append(result)
    text = "\n".join(result_list)
    yield text
