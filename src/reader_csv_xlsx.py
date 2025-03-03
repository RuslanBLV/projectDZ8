
import pandas as pd
import csv


def reader_csv(path):
    """Выводит список словарей странзакций из файла .csv"""
    with open(path) as file:
        wine_reviews = csv.DictReader(file)
        trans = []
        for row in wine_reviews:
            trans.append(row)
        return trans


# print(reader_csv("../transactions.csv"))


def reader_excel(path):
    """Выводит список словарей странзакций из файла .xlsx"""
    pf = pd.read_excel(path)
    file_dataframe = pd.DataFrame(pf)
    file_dict = file_dataframe.to_dict(orient='records')
    return file_dict


# print(reader_excel("../transactions_excel.xlsx"))

