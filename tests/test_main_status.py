# -*- coding: utf-8 -*-
from src.main_status import (select_type_welcome, status_filter, sort_reverse_true_false, trans_rub,
                             trans_rub_xlsx_csv, filter_trans_word)
import unittest
from unittest.mock import patch
from src.utils import result_list
from src.reader_csv_xlsx import list_scv
from src.processing import sort_by_date


class test_select_type_welcome_class(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_select_type_welcome_1(self, mock_input):
        result = select_type_welcome()
        self.assertEqual(result, "Для обработки выбран JSON-файл.")

    @patch('builtins.input', side_effect=['2'])
    def test_select_type_welcome_2(self, mock_input):
        result = select_type_welcome()
        self.assertEqual(result, "Для обработки выбран CSV-файл.")

    @patch('builtins.input', side_effect=['3'])
    def test_select_type_welcome_3(self, mock_input):
        result = select_type_welcome()
        self.assertEqual(result, "Для обработки выбран XLSX-файл.")


class test_status_filter_class(unittest.TestCase):
    @patch('builtins.input', side_effect=['EXECUTED'])
    def test_status_filter_executed(self, mock_input):
        result = status_filter()
        self.assertEqual(result, "Операции отфильтрованы по статусу 'EXECUTED'")

    @patch('builtins.input', side_effect=['CANCELED'])
    def test_status_filter_canceled(self, mock_input):
        result = status_filter()
        self.assertEqual(result, "Операции отфильтрованы по статусу 'CANCELED'")

    @patch('builtins.input', side_effect=['PENDING'])
    def test_status_filter_pending(self, mock_input):
        result = status_filter()
        self.assertEqual(result, "Операции отфильтрованы по статусу 'PENDING'")


class test_sort_reverse_true_false_class(unittest.TestCase):
    @patch('builtins.input', side_effect=['да', 'по возрастанию'])
    def test_sort_reverse_true_false_1(self, mock_input):
        result = sort_reverse_true_false(result_list)
        reverse_data = sort_by_date(result_list, reverse=False)
        self.assertEqual(result, reverse_data)

    @patch('builtins.input', side_effect=['да', 'по убыванию'])
    def test_sort_reverse_true_false_2(self, mock_input):
        result = sort_reverse_true_false(result_list)
        reverse_data = sort_by_date(result_list, reverse=True)
        self.assertEqual(result, reverse_data)

    @patch('builtins.input', side_effect=['нет'])
    def test_sort_reverse_true_false_3(self, mock_input):
        result = sort_reverse_true_false(result_list)
        reverse_data = result_list
        self.assertEqual(result, reverse_data)


class test_trans_rub_class(unittest.TestCase):
    @patch('builtins.input', side_effect=['да'])
    def test_trans_rub_1(self, mock_input):
        result = trans_rub(result_list)
        list_rub = []
        for i in result_list:
            if i["operationAmount"]["currency"]["code"] == "RUB":
                list_rub.append(i)
        self.assertEqual(result, list_rub)

    @patch('builtins.input', side_effect=['нет'])
    def test_trans_rub_2(self, mock_input):
        result = trans_rub(result_list)
        self.assertEqual(result, result_list)


class test_trans_rub_xlsx_csv_class(unittest.TestCase):
    @patch('builtins.input', side_effect=['да'])
    def test_trans_rub_1(self, mock_input):
        result = trans_rub_xlsx_csv(list_scv)
        list_rub = []
        for i in list_scv:
            if i["currency_code"] == "RUB":
                list_rub.append(i)
        self.assertEqual(result, list_rub)

    @patch('builtins.input', side_effect=['нет'])
    def test_trans_rub_2(self, mock_input):
        result = trans_rub_xlsx_csv(list_scv)
        self.assertEqual(result, list_scv)


class test_filter_trans_word_class(unittest.TestCase):
    @patch('builtins.input', side_effect=['да', 'Перевод организации'])
    def test_filter_trans_word_1(self, mock_input):
        result = filter_trans_word(list_scv)
        trans = []
        for i in list_scv:
            if i["description"] == "Перевод организации":
                trans.append(i)
        self.assertEqual(result, trans)

    @patch('builtins.input', side_effect=['нет'])
    def test_filter_trans_word_2(self, mock_input):
        result = filter_trans_word(list_scv)
        self.assertEqual(result, list_scv)

    @patch('builtins.input', side_effect=['да', 'вфывыф'])
    def test_filter_trans_word_3(self, mock_input):
        result = filter_trans_word(list_scv)
        self.assertEqual(result, [])
