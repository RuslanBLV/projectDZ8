import pytest
from decorators import log, log_generator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions, \
    transactions_clear
from src.masks import get_mask_account, get_mask_card_number
from src.wedget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("card_numbers, expected",
                         [("7000792289606361", "get_mask_card_number ok: 7000 79** **** 6361\n\n"),
                          ("7000792284625144", "get_mask_card_number ok: 7000 79** **** 5144\n\n"),
                          ("7000792784321548", "get_mask_card_number ok: 7000 79** **** 1548\n\n"),
                          ("7000746848516547", "get_mask_card_number ok: 7000 74** **** 6547\n\n"),
                          ("", "get_mask_card_number ok: wrong number\n\n"),
                          ("7000792284625144515415", "get_mask_card_number ok: wrong number\n\n")])
def test_log_get_mask_card_number(capsys, card_numbers, expected):
    get_mask_card_number(card_numbers)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("card_numbers, expected", [("35383033474447895560", "get_mask_account ok: **5560\n\n"),
                                                    ("35383033474447484114", "get_mask_account ok: **4114\n\n"),
                                                    ("35383033474156454788", "get_mask_account ok: **4788\n\n"),
                                                    ("", "get_mask_account ok: Incorrect account entered\n\n"),
                                                    ("3538303347415645478854551", "get_mask_account ok: Incorrect "
                                                                                  "account entered\n\n")])
def test_log_get_mask_account(capsys, card_numbers, expected):
    get_mask_account(card_numbers)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_log_filter_by_state(capsys):
    list_state = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    filter_by_state(list_state)
    captured = capsys.readouterr()
    assert captured.out == ("filter_by_state ok: [{'id': 41428829, 'state': 'EXECUTED', 'date': "
                            "'2019-07-03T18:35:29.512364'},"
                            " {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n"
                            "[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},"
                            " {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]\n\n")


def test_log_sort_by_date(capsys):
    sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
    captured = capsys.readouterr()
    assert captured.out == ("sort_by_date ok: [{'id': 41428829, 'state': 'EXECUTED', 'date': "
                            "'2019-07-03T18:35:29.512364'},"
                            " {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},"
                            " {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},"
                            " {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n\n")


@pytest.mark.parametrize("card_and_account, expected",
                         [("Visa Platinum 7000792289606361", "mask_account_card ok: Visa Platinum 7000 79** **** "
                                                             "6361\n\n"),
                          ("Maestro 7000792289606361", "mask_account_card ok: Maestro 7000 79** **** 6361\n\n"),
                          ("Счет 73654108430135874305", "mask_account_card ok: Счет **4305\n\n"),
                          ("Счет 35383033474447895560", "mask_account_card ok: Счет **5560\n\n"),
                          ("Счет 35383033474447895560456111", "mask_account_card ok: Invalid account\n\n"),
                          ("Maestro 7000792289606361545154154", "mask_account_card ok: Invalid card number\n\n"),
                          ("Maestroooooo 7000792289606361",
                           "mask_account_card ok: You entered an incorrect card or account name\n\n")])
def test_log_mask_account_card(capsys, card_and_account, expected):
    mask_account_card(card_and_account)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize("data, expected", [("2024-03-11T02:26:18.671407", "get_date ok: 11.03.2024\n\n"),
                                            ("2021-06-08T01:24:17.784123", "get_date ok: 08.06.2021\n\n"),
                                            ("2024/03/11T02:26:18.671407", "get_date ok: Invalid date\n\n"),
                                            ("2024-03-11T02-26-18-671407", "get_date ok: Invalid date\n\n"),
                                            ("", "get_date ok: Invalid date\n\n")])
def test_log_get_date(capsys, data, expected):
    get_date(data)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_log_generator_filter_by_currency(capsys):
    generator_usd = filter_by_currency(transactions, "USD")
    assert (next(generator_usd)) == ("filter_by_currency ok: {'id': 939719570, 'state': 'EXECUTED',"
                                     " 'date': '2018-06-30T02:08:58.425572', 'operationAmount':"
                                     " {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},"
                                     " 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',"
                                     " 'to': 'Счет 11776614605963066702'}\n")
    assert (next(generator_usd)) == ("filter_by_currency ok: {'id': 142264268, 'state': 'EXECUTED',"
                                     " 'date': '2019-04-04T23:20:05.206878', 'operationAmount':"
                                     " {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},"
                                     " 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',"
                                     " 'to': 'Счет 75651667383060284188'}\n")
    assert (next(generator_usd)) == ("filter_by_currency ok: {'id': 895315941, 'state': 'EXECUTED',"
                                     " 'date': '2018-08-19T04:27:37.904916', 'operationAmount':"
                                     " {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},"
                                     " 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',"
                                     " 'to': 'Visa Platinum 8990922113665229'}\n")
    generator_rub = filter_by_currency(transactions, "RUB")
    assert (next(generator_rub)) == ("filter_by_currency ok: {'id': 873106923, 'state': 'EXECUTED',"
                                     " 'date': '2019-03-23T01:09:46.296404', 'operationAmount':"
                                     " {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},"
                                     " 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',"
                                     " 'to': 'Счет 74489636417521191160'}\n")
    assert (next(generator_rub)) == ("filter_by_currency ok: {'id': 594226727, 'state': 'CANCELED',"
                                     " 'date': '2018-09-12T21:27:25.241689', 'operationAmount':"
                                     " {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},"
                                     " 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',"
                                     " 'to': 'Счет 14211924144426031657'}\n")
    generator_transactions_clear = filter_by_currency(transactions_clear, "RUB")
    assert (next(generator_transactions_clear)) == "filter_by_currency ok: Список пуст\n"
    generator_transactions_error = filter_by_currency(transactions, "Неизвестный")
    assert (next(generator_transactions_error)) == "filter_by_currency ok: Нет такой валюты\n"


def test_log_generator_transaction_descriptions(capsys):
    right = transaction_descriptions(transactions)
    assert (next(right)) == "transaction_descriptions ok: Перевод организации\n"
    assert (next(right)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(right)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(right)) == "transaction_descriptions ok: Перевод с карты на карту\n"
    clear_list = transaction_descriptions(transactions_clear)
    assert (next(clear_list)) == "transaction_descriptions ok: Список пуст\n"
    limit_list = transaction_descriptions(transactions)
    assert (next(limit_list)) == "transaction_descriptions ok: Перевод организации\n"
    assert (next(limit_list)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(limit_list)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(limit_list)) == "transaction_descriptions ok: Перевод с карты на карту\n"
    assert (next(limit_list)) == "transaction_descriptions ok: Перевод организации\n"
    assert (next(limit_list)) == "transaction_descriptions ok: Список закончился\n"


def test_log_generator_card_number_generator(capsys):
    right = card_number_generator(1, 10)
    assert (next(right)) == ("card_number_generator ok: 0000 0000 0000 0001\n0000 0000 0000 0002\n0000 0000 0000 0003\n"
                             "0000 0000 0000 0004\n0000 0000 0000 0005\n0000 0000 0000 0006\n0000 0000 0000 0007\n"
                             "0000 0000 0000 0008\n0000 0000 0000 0009\n0000 0000 0000 0010\n")
    error = card_number_generator(1, 10000000000000000)
    assert (next(error)) == "card_number_generator ok: Неверный лимит\n"
    max_numbers = card_number_generator(9999999999999990, 9999999999999999)
    assert (next(max_numbers)) == ("card_number_generator ok: 9999 9999 9999 9990\n9999 9999 9999 9991\n"
                                   "9999 9999 9999 9992\n9999 9999 9999 9993\n9999 9999 9999 9994\n"
                                   "9999 9999 9999 9995\n9999 9999 9999 9996\n9999 9999 9999 9997\n"
                                   "9999 9999 9999 9998\n9999 9999 9999 9999\n")
