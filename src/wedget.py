from decorators import log

@log()
def mask_account_card(account_number: list):
    """Маскировка номера или счета"""
    numbers = ""
    letters = ""
    for number in account_number:
        if number.isdigit():
            numbers += number
        elif not number.isdigit():
            letters += number
    if letters in [
        "Maestro ",
        "Visa Gold ",
        "Visa Platinum ",
        "Visa Classic ",
        "MasterCard ",
        "Счет ",
    ]:
        if letters == "Счет ":
            if len(numbers) == 20:
                mask_numbers = f"**{numbers[-4:]}"
                return letters + mask_numbers
            else:
                return "Неверный счет"
        elif letters != "Счет ":
            if len(numbers) == 16:
                mask_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
                return letters + mask_numbers
            else:
                return "Неверный номер карты"
    else:
        return "Вы ввели неверное название карты или счета"

@log()
def get_date(data: str) -> str:
    """Сортировка даты"""
    if len(data) == 26:
        if (
            data[4] == "-"
            and data[7] == "-"
            and data[13] == ":"
            and data[16] == ":"
            and data[19] == "."
        ):
            new_data = f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
            return new_data
        else:
            return "Неверная дата"
    else:
        return "Неверная дата"
