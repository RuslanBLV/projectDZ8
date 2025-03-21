# -*- coding: utf-8 -*-
import pandas as pd
import csv


def reader_csv(path):
    """Выводит список словарей странзакций из файла .csv"""
    list_csv = []
    with open(path) as file:
        wine_reviews = csv.DictReader(file, delimiter=";")
        for row in wine_reviews:
            if any(row.values()):
                list_csv.append(row)
    return list_csv


list_scv = reader_csv("../transactions.csv")


def reader_excel(path):
    """Выводит список словарей странзакций из файла .xlsx"""
    pf = pd.read_excel(path)
    df_cleaned = pf.dropna(how='all')
    file_dataframe = pd.DataFrame(df_cleaned)
    file_dicts = file_dataframe.to_dict(orient='records')
    return file_dicts


excel_list = reader_excel("../transactions_excel.xlsx")
