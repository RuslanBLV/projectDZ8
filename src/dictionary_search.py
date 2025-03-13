# -*- coding: utf-8 -*-
import re
from collections import Counter


def search_operations(transactions: list, search: str) -> list:
    transactions_list = []
    for trans in transactions:
        descriptions = trans.get("description")
        if re.search(search, descriptions, flags=re.IGNORECASE) is not None:
            transactions_list.append(trans)
    return transactions_list


descriptions = ["Перевод с карты на карту", "Перевод организации", "Перевод со счета на счет"]


def banking_transactions(description: list, transaction: list):
    description_list = []
    for trans in transaction:
        if trans["description"] in description:
            description_list.append(trans["description"])
    counted = Counter(description_list)
    return counted
