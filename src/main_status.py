# -*- coding: utf-8 -*-
import re
from src.utils import result_list
from src.reader_csv_xlsx import list_scv, excel_list
from src.processing import sort_by_date
from src.wedget import get_date, mask_account_card
from collections import Counter


def select_type_welcome():
    """Фильтрация по номеру пункта типа файла"""
    while True:
        user_info = int(input("Программа: Привет! Добро пожаловать в программу работы\n"
                              "с банковскими транзакциями.\n"
                              "Выберите необходимый пункт меню:\n"
                              "1. Получить информацию о транзакциях из JSON-файла\n"
                              "2. Получить информацию о транзакциях из CSV-файла\n"
                              "3. Получить информацию о транзакциях из XLSX-файла\n"
                              "Введите номер пункта: "))  # Хранится номер пункта типа файла
        if user_info == 1:
            return "Для обработки выбран JSON-файл."
        elif user_info == 2:
            return "Для обработки выбран CSV-файл."
        elif user_info == 3:
            return "Для обработки выбран XLSX-файл."
        else:
            print("Есть только 3 пункта: '1', '2', '3'")


def status_filter():
    """Фильтрация списка по статусу транзакции"""
    while True:
        user_status = str(input("Статусы, по которому необходимо выполнить фильтрацию.\n"
                                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                                "Введите статус: "))  # Хранится статус фильтрации списка
        user_status_lower = user_status.upper()
        if user_status_lower == "EXECUTED":
            return "Операции отфильтрованы по статусу 'EXECUTED'"
        elif user_status_lower == "CANCELED":
            return "Операции отфильтрованы по статусу 'CANCELED'"
        elif user_status_lower == "PENDING":
            return "Операции отфильтрованы по статусу 'PENDING'"
        else:
            print("Есть только три статуса: EXECUTED, CANCELED, PENDING")


def sort_reverse_true_false(list_trans):
    """Сортировка по дате"""
    while True:
        user_data = str(input("Отсортировать операции по дате? Да/Нет\nВведите: ")).lower()
        if user_data == "да":
            while True:
                user_reverse = str(input("Отсортировать по возрастанию или по убыванию?\nВведите: ")).lower()
                if user_reverse == "по возрастанию":
                    if len(list_trans) == 0:
                        return list_trans
                    else:
                        reverse_data = sort_by_date(list_trans, reverse=False)
                        return reverse_data
                elif user_reverse == "по убыванию":
                    if len(list_trans) == 0:
                        return list_trans
                    else:
                        reverse_data = sort_by_date(list_trans, reverse=True)
                        return reverse_data
                else:
                    print("Есть только два ввода: 'по возрастанию' и 'по убыванию'\nВведите: ")
        elif user_data == "нет":
            return list_trans
        else:
            print("Есть только два ввода: 'да' и 'нет'")


def trans_rub(list_trans):
    """Выводит рублевые транзакции из json файла"""
    while True:
        user_rub = str(input("Выводить только рублевые тразакции? Да/Нет\nВведите: ")).lower()
        list_rub = []
        if user_rub == "да":
            for i in list_trans:
                if i["operationAmount"]["currency"]["code"] == "RUB":
                    list_rub.append(i)
            return list_rub
        elif user_rub == "нет":
            return list_trans
        else:
            print("Есть только два ввода: 'да' и 'нет'")


def trans_rub_xlsx_csv(list_trans):
    """Выводит рублевые транзакции из xlsx и csv файлов"""
    while True:
        user_rub = str(input("Выводить только рублевые тразакции? Да/Нет\nВведите: ")).lower()
        list_rub = []
        if user_rub == "да":
            if len(list_trans) == 0:
                return list_trans
            else:
                for i in list_trans:
                    if i["currency_code"] == "RUB":
                        list_rub.append(i)
                return list_rub
        elif user_rub == "нет":
            return list_trans
        else:
            print("Есть только два ввода: 'да' и 'нет'")


def filter_trans_word(list_trans):
    """Сортировка по слову"""
    while True:
        user_word_question = str(
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nВведите: ")).lower()
        if user_word_question == "да":
            user_word = str(input("Введите слово: "))
            list_trans_sort_word = []
            for i in list_trans:
                if i["description"] == user_word:
                    list_trans_sort_word.append(i)
            if len(list_trans_sort_word) == 0:
                return []
            else:
                return list_trans_sort_word
        elif user_word_question == "нет":
            return list_trans
        else:
            print("Есть только два ввода: 'да' и 'нет'")


def display_trans(list_trans):
    """Выводит транзакции на дисплей json файла"""
    try:
        number = [i["description"] for i in list_trans]
        number_count = Counter(number)
        if len(list_trans) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print(f"Всего банковских операций в выборке: {number_count}\n")
            for i in list_trans:
                if i["description"] == "Открытие вклада":
                    print(f"{get_date(i["date"])} {i["description"]}\n"
                          f"{mask_account_card(i["to"])}\n"
                          f"Сумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["code"]}\n\n")
                else:
                    print(f"{get_date(i["date"])} {i["description"]}\n"
                          f"{mask_account_card(i["from"])} -> {mask_account_card(i["to"])}\n"
                          f"Сумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["code"]}\n\n")
    except TypeError:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def display_trans_xlsx_csv(list_trans):
    """Выводит транзакции на дисплей xlsx и csv файлов"""
    try:
        number = [i["description"] for i in list_trans]
        number_count = Counter(number)
        if len(list_trans) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print(f"Всего банковских операций в выборке: {number_count}\n")
            for i in list_trans:
                if i["description"] == "Открытие вклада":
                    print(f"{get_date(i["date"])} {i["description"]}\n"
                          f"{mask_account_card(i["to"])}\n"
                          f"Сумма: {i["amount"]} {i["currency_code"]}\n\n")
                else:
                    print(f"{get_date(i["date"])} {i["description"]}\n"
                          f"{mask_account_card(i["from"])} -> {mask_account_card(i["to"])}\n"
                          f"Сумма: {i["amount"]} {i["currency_code"]}\n\n")
    except TypeError:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def file_type_status():
    """Логика всех функций"""
    result_func_tupe = select_type_welcome()
    if result_func_tupe == "Для обработки выбран JSON-файл.":
        result_func_status = status_filter()
        if result_func_status == "Операции отфильтрованы по статусу 'EXECUTED'":
            pattern_1 = re.compile(r"EXECUTED")
            executed_pattern = [result for result in result_list if pattern_1.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(executed_pattern)
            list_rub = trans_rub(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans(list_filter_word)
        elif result_func_status == "Операции отфильтрованы по статусу 'CANCELED'":
            pattern_2 = re.compile(r"CANCELED")
            canceled_pattern = [result for result in result_list if pattern_2.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(canceled_pattern)
            list_rub = trans_rub(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans(list_filter_word)
        elif result_func_status == "Операции отфильтрованы по статусу 'PENDING'":
            pattern_3 = re.compile(r"PENDING")
            pending_pattern = [result for result in result_list if pattern_3.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(pending_pattern)
            list_rub = trans_rub(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans(list_filter_word)
    elif result_func_tupe == "Для обработки выбран CSV-файл.":
        result_func_status = status_filter()
        if result_func_status == "Операции отфильтрованы по статусу 'EXECUTED'":
            pattern_4 = re.compile(r"EXECUTED")
            executed_pattern = [result for result in list_scv if pattern_4.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(executed_pattern)
            list_rub = trans_rub_xlsx_csv(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            print(list_filter_word)
            return display_trans_xlsx_csv(list_filter_word)
        elif result_func_status == "Операции отфильтрованы по статусу 'CANCELED'":
            pattern_5 = re.compile(r"CANCELED")
            canceled_pattern = [result for result in list_scv if pattern_5.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(canceled_pattern)
            print(list_reverse_data)
            list_rub = trans_rub_xlsx_csv(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans_xlsx_csv(list_filter_word)
        elif result_func_status == "Операции отфильтрованы по статусу 'PENDING'":
            pattern_6 = re.compile(r"PENDING")
            pending_pattern = [result for result in list_scv if pattern_6.search(result["state"])]
            print(pending_pattern)
            list_reverse_data = sort_reverse_true_false(pending_pattern)
            print(list_reverse_data)
            list_rub = trans_rub_xlsx_csv(list_reverse_data)
            # print(list_rub)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans_xlsx_csv(list_filter_word)
    elif result_func_tupe == "Для обработки выбран XLSX-файл.":
        result_func_status = status_filter()
        if result_func_status == "Операции отфильтрованы по статусу 'EXECUTED'":
            pattern_7 = re.compile(r"EXECUTED")
            executed_pattern = [result for result in excel_list if pattern_7.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(executed_pattern)
            list_rub = trans_rub_xlsx_csv(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans_xlsx_csv(list_filter_word)
        elif result_func_status == "Операции отфильтрованы по статусу 'CANCELED'":
            pattern_8 = re.compile(r"CANCELED")
            canceled_pattern = [result for result in excel_list if pattern_8.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(canceled_pattern)
            list_rub = trans_rub_xlsx_csv(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans_xlsx_csv(list_filter_word)
        elif result_func_status == "Операции отфильтрованы по статусу 'PENDING'":
            pattern_9 = re.compile(r"PENDING")
            pending_pattern = [result for result in excel_list if pattern_9.search(result["state"])]
            list_reverse_data = sort_reverse_true_false(pending_pattern)
            list_rub = trans_rub_xlsx_csv(list_reverse_data)
            list_filter_word = filter_trans_word(list_rub)
            return display_trans_xlsx_csv(list_filter_word)
