def filter_by_state(stats):
    """ Сортировка по ключу "state": "EXECUTED" или "CANCELED" """
    executed = []
    canceled = []
    for stat in stats:
        if stat["state"] == "EXECUTED":
            executed.append(stat)
        elif stat["state"] == "CANCELED":
            canceled.append(stat)
    return (f"""{executed}
{canceled}""")

def sort_by_date(data: str, reverse: bool=True) -> list:
    """Сортировка даты по убыванию"""
    return sorted(data, key= lambda x: x["date"], reverse=reverse)