import pytest
from decorators import log, log_generator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions
from src.masks import get_mask_account, get_mask_card_number
from src.wedget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


def test_log(capsys):
    get_mask_card_number("7000792289606361")
    captured = capsys.readouterr()
    assert captured.out == "get_mask_card_number ok: 7000 79** **** 6361\n\n"


def test_log(capsys):
    get_mask_account("35383033474447895560")
    captured = capsys.readouterr()
    assert captured.out == "get_mask_account ok: **5560\n\n"


def test_log(capsys):
    filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
    captured = capsys.readouterr()
    assert captured.out == ("filter_by_state ok: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},"
                            " {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n"
                            "[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},"
                            " {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]\n\n")


def test_log(capsys):
    sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
    captured = capsys.readouterr()
    assert captured.out == ("sort_by_date ok: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},"
                            " {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},"
                            " {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},"
                            " {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n\n")


def test_log(capsys):
    mask_account_card("Maestro 7000792289606361")
    captured = capsys.readouterr()
    assert captured.out == "mask_account_card ok: Maestro 7000 79** **** 6361\n\n"


def test_log(capsys):
    get_date("2024-03-11T02:26:18.671407")
    captured = capsys.readouterr()
    assert captured.out == "get_date ok: 11.03.2024\n\n"


def test_log_generator(capsys):
    gen = filter_by_currency(transactions, "USD")
    assert (next(gen)) == ("filter_by_currency ok: {'id': 939719570, 'state': 'EXECUTED', 'date': "
                           "'2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', "
                           "'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод "
                           "организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет "
                           "11776614605963066702'}\n")
    assert (next(gen)) == ("filter_by_currency ok: {'id': 142264268, 'state': 'EXECUTED', 'date': "
                           "'2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', "
                           "'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со "
                           "счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет "
                           "75651667383060284188'}\n")
    assert (next(gen)) == ("filter_by_currency ok: {'id': 895315941, 'state': 'EXECUTED', 'date': "
                           "'2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', "
                           "'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты "
                           "на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum "
                           "8990922113665229'}\n")


def test_log_generator(capsys):
    gen = transaction_descriptions(transactions)
    assert (next(gen)) == "transaction_descriptions ok: Перевод организации\n"
    assert (next(gen)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(gen)) == "transaction_descriptions ok: Перевод со счета на счет\n"
    assert (next(gen)) == "transaction_descriptions ok: Перевод с карты на карту\n"
    assert (next(gen)) == "transaction_descriptions ok: Перевод организации\n"
    assert (next(gen)) == "transaction_descriptions ok: Список закончился\n"


def test_log_generator(capsys):
    gen = card_number_generator(1, 3)
    assert (next(gen)) == ('card_number_generator ok: 0000 0000 0000 0001\n'
                           '0000 0000 0000 0002\n'
                           '0000 0000 0000 0003\n')










