import pytest
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    list_state = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    result_executed = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    result_canceled = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    assert filter_by_state(list_state) == f"""{result_executed}
{result_canceled}"""


def test_filter_by_state_none_executed():
    canceled = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    assert filter_by_state([{'id': 41428829, 'state': 'EXE', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXE', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == f"""нет данных по статусу EXECUTED
f"{canceled}"""


def test_filter_by_state_none_canceled():
    executed = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CAN', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CAN', 'date': '2018-10-14T08:21:33.419441'}]) == f"""нет данных по статусу CANCELED
f"{executed}"""


def test_filter_by_state_none_canceled_executed():
    assert filter_by_state([{'id': 41428829, 'state': 'EXE', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXE', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CAN', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CAN', 'date': '2018-10-14T08:21:33.419441'}]) == "нет данных по статусу CANCELED и EXECUTED"


def test_sort_by_date_reverse_true():
    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    assert sort_by_date(list_data) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_reverse_false():
    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    assert sort_by_date(list_data, False) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date_identical():
    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]
    assert sort_by_date(list_data) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]


def test_sort_by_date_error():
    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '20190703T18.35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-0703T18:35:29.512364'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21.2725.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T1835:29512364'}]
    assert sort_by_date(list_data) == "Неверная дата в списке"
