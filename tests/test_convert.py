import pytest
from unittest.mock import Mock
from unittest.mock import patch
from src.utils import amount_transactions, financial_transactions, result


@pytest.mark.parametrize("trans, expected",
                         [([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",
                             "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                             "description": "Перевод организации", "from": "MasterCard 7158300734726758",
                             "to": "Счет 35383033474447895560"}], {'success': True,
                                                                   'query': {'from': 'USD', 'to': 'RUB',
                                                                             'amount': 8221.37},
                                                                   'info': {'timestamp': 1740657851, 'rate': 86.786867},
                                                                   'date': '2025-02-27', 'result': 713506.944748}),
                          ([{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                             "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                             "description": "Перевод организации", "from": "Maestro 1596837868705199",
                             "to": "Счет 64686473678894779589"}],
                           {'success': True, 'query': {'from': 'RUB', 'to': 'RUB', 'amount': 31957.58},
                            'info': {'timestamp': 1740673992, 'rate': 1}, 'date': '2025-02-27',
                            'result': 31957.58})])
@patch('requests.get')
def test_transactions_convert(mock_get, trans, expected):
    mock_get.return_value.json.return_value = expected
    assert amount_transactions(trans) == round(mock_get.return_value.json.return_value["result"], 2)


@pytest.mark.parametrize("trans, expected", [("../data/operations.json", result), ("../data/operations.jso", [])])
def test_financial_transactions(trans, expected):
    assert financial_transactions(trans) == expected
