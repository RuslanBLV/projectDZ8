from decorators import log
from src.utils import result_list


@log()
def filter_by_state(stats: list) -> str:
    """Сортировка по ключу "state": "EXECUTED" или "CANCELED" """
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
    return f"""{executed}
{canceled}"""


def sort_by_date(data: list, reverse: bool = True):
    """Сортировка даты по убыванию"""
    for list_data in data:
        if len(list_data["date"]) >= 20:
            filtered_data = filter(lambda x: 'date' in x, data)
            return sorted(filtered_data, key=lambda x: x["date"], reverse=reverse)
        else:
            return "Неверная дата в списке"


list_json_reverse_false = sort_by_date(result_list, reverse=False)
