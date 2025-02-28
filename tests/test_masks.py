import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "get_mask_card_number ok: 7000 79** **** 6361\n"


def test_get_mask_card_number_len():
    assert get_mask_card_number("") == "get_mask_card_number ok: wrong number\n"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "get_mask_account ok: **4305\n"

def test_get_mask_account_len():
        assert get_mask_account("") == "get_mask_account ok: Incorrect account entered\n"







