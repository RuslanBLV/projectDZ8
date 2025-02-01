def filter_by_state(stats: list) -> list:
    """ Сортировка по ключу "state": "EXECUTED" или "CANCELED" """
    executed = []
    canceled = []
    for stat in stats:
        if stat["state"] == "EXECUTED":
            executed.append(stat)
        elif stat["state"] == "CANCELED":
            canceled.append(stat)
    if executed == [] and canceled != []:
        return f"""нет данных по статусу EXECUTED
f"{canceled}"""
    elif executed != [] and canceled == []:
        return f"""нет данных по статусу CANCELED
f"{executed}"""
    elif executed == [] and canceled == []:
        return "нет данных по статусу CANCELED и EXECUTED"
    return (f"""{executed}
{canceled}""")

def sort_by_date(data: str, reverse: bool=True) -> list:
    """Сортировка даты по убыванию"""
    for list_data in data:
        if len(list_data["date"]) == 26:
            return sorted(data, key= lambda x: x["date"], reverse=reverse)
        else:
            return "Неверная дата в списке"

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]))