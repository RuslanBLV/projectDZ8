import pytest

from src.wedget import mask_account_card, get_date

@pytest.mark.parametrize("card_and_account, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                                        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                                                        ("Счет 73654108430135874305", "Счет **4305"),
                                                        ("Счет 35383033474447895560", "Счет **5560"),])
def test_mask_account_card(card_and_account, expected):
    """Правильная работа функции "маскировка карты или счета" """
    assert mask_account_card(card_and_account) == expected


def test_mask_account_card_error():
    """Ошибка в наборе названия карты или счета"""
    assert mask_account_card("errorname 7000792289606361") == "You entered an incorrect card or account name"


def test_mask_account_numbers():
    """Ошибка в наборе номера счета"""
    assert mask_account_card("Счет 3538303347") == "Неверный счет"


def test_mask_card_numbers():
    """ошибка в наборе номера карты"""
    assert mask_account_card("Maestro 70007922896") == "Неверный номер карты"


def test_get_data():
    """Проверка правильности сортировки даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

@pytest.mark.parametrize("data_error, expected", [("2024/03/11T02:26:18.671407", "Invalid date"),
                                                  ("2024-03-11T02-26-18-671407", "Invalid date"),
                                                  ("2024.03.11T02.26.18.671407", "Invalid date"),
                                                  ("2024:03:11T02:26:18.671407", "Invalid date")])
def test_get_data_error(data_error, expected):
    """Возможные ошибки ввода даты для сортировки"""
    assert get_date(data_error) == expected