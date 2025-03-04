from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
    transactions,
    transactions_clear,
)


def test_filter_by_currency():
    generator_usd = filter_by_currency(transactions, "USD")
    assert (
            (next(generator_usd))
            == "filter_by_currency ok: {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',"
               " 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},"
               " 'description': 'Перевод организации',"
               " 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}\n"
    )
    assert (
            (next(generator_usd))
            == "filter_by_currency ok: {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',"
               " 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},"
               " 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',"
               " 'to': 'Счет 75651667383060284188'}\n"
    )
    assert (
            (next(generator_usd))
            == "filter_by_currency ok: {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',"
               " 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},"
               " 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',"
               " 'to': 'Visa Platinum 8990922113665229'}\n"
    )
    generator_rub = filter_by_currency(transactions, "RUB")
    assert (
            (next(generator_rub))
            == "filter_by_currency ok: {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',"
               " 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},"
               " 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',"
               " 'to': 'Счет 74489636417521191160'}\n"
    )
    assert (
            (next(generator_rub))
            == "filter_by_currency ok: {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', "
               "'operationAmount':"
               " {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': "
               "'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}\n"
    )
    generator_transactions_clear = filter_by_currency(transactions_clear, "RUB")
    assert (
               next(generator_transactions_clear)
           ) == "filter_by_currency ok: Список пуст\n"
    generator_transactions_error = filter_by_currency(transactions, "Неизвестный")
    assert (
               next(generator_transactions_error)
           ) == "filter_by_currency ok: Нет такой валюты\n"


def test_transaction_descriptions():
    right = transaction_descriptions(transactions)
    assert (next(right)) == "transaction_descriptions ok: Перевод организации\n"
    assert (next(right)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(right)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(right)) == "transaction_descriptions ok: Перевод с карты на карту\n"
    clear_list = transaction_descriptions(transactions_clear)
    assert (next(clear_list)) == "transaction_descriptions ok: Список пуст\n"
    limit_list = transaction_descriptions(transactions)
    assert (next(limit_list)) == "transaction_descriptions ok: Перевод организации\n"
    assert (
               next(limit_list)
           ) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (
               next(limit_list)
           ) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (
               next(limit_list)
           ) == "transaction_descriptions ok: Перевод с карты на карту\n"
    assert (next(limit_list)) == "transaction_descriptions ok: Перевод организации\n"
    assert (next(limit_list)) == "transaction_descriptions ok: Список закончился\n"


def test_card_number_generator():
    right = card_number_generator(1, 10)
    assert (next(right)) == (
        "card_number_generator ok: 0000 0000 0000 0001\n0000 0000 0000 0002\n"
        "0000 0000 0000 0003\n0000 0000 0000 0004\n"
        "0000 0000 0000 0005\n0000 0000 0000 0006\n"
        "0000 0000 0000 0007\n0000 0000 0000 0008\n"
        "0000 0000 0000 0009\n0000 0000 0000 0010\n"
    )
    error = card_number_generator(1, 10000000000000000)
    assert (next(error)) == "card_number_generator ok: Неверный лимит\n"
    max_numbers = card_number_generator(9999999999999990, 9999999999999999)
    assert (next(max_numbers)) == (
        "card_number_generator ok: 9999 9999 9999 9990\n9999 9999 9999 9991\n"
        "9999 9999 9999 9992\n9999 9999 9999 9993\n"
        "9999 9999 9999 9994\n9999 9999 9999 9995\n"
        "9999 9999 9999 9996\n9999 9999 9999 9997\n"
        "9999 9999 9999 9998\n9999 9999 9999 9999\n"
    )
