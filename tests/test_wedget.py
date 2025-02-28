import pytest

from src.wedget import mask_account_card, get_date

@pytest.mark.parametrize("card_and_account, expected", [("Visa Platinum 7000792289606361", "mask_account_card ok: Visa Platinum 7000 79** **** 6361\n"),
                                                        ("Maestro 7000792289606361", "mask_account_card ok: Maestro 7000 79** **** 6361\n"),
                                                        ("Счет 73654108430135874305", "mask_account_card ok: Счет **4305\n"),
                                                        ("Счет 35383033474447895560", "mask_account_card ok: Счет **5560\n"),])
def test_mask_account_card(card_and_account, expected):
    """Правильная работа функции "маскировка карты или счета" """
    assert mask_account_card(card_and_account) == expected


def test_mask_account_card_error():
    """Ошибка в наборе названия карты или счета"""
    assert mask_account_card("errorname 7000792289606361") == "mask_account_card ok: You entered an incorrect card or account name\n"


def test_mask_account_numbers():
    """Ошибка в наборе номера счета"""
    assert mask_account_card("Счет 3538303347") == "mask_account_card ok: Invalid account\n"


def test_mask_card_numbers():
    """ошибка в наборе номера карты"""
    assert mask_account_card("Maestro 70007922896") == "mask_account_card ok: Invalid card number\n"


def test_get_data():
    """Проверка правильности сортировки даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "get_date ok: 11.03.2024\n"

@pytest.mark.parametrize("data_error, expected", [("2024/03/11T02:26:18.671407", "get_date ok: Invalid date\n"),
                                                  ("2024-03-11T02-26-18-671407", "get_date ok: Invalid date\n"),
                                                  ("2024.03.11T02.26.18.671407", "get_date ok: Invalid date\n"),
                                                  ("2024:03:11T02:26:18.671407", "get_date ok: Invalid date\n")])
def test_get_data_error(data_error, expected):
    """Возможные ошибки ввода даты для сортировки"""
    assert get_date(data_error) == expected