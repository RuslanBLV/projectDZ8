def mask_account_card(account_number: str) -> str:
    """Маскировка номера или счета"""
    numbers = ""
    letters = ""
    for number in account_number:
        if number.isdigit():
            numbers += number
        elif not number.isdigit():
            letters += number
    if letters == "Счет ":
        mask_numbers = f"**{numbers[-4:]}"
    elif letters != "Счет ":
        mask_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"

    return letters + mask_numbers


def get_date(data: str) -> str:
    """Сортировка даты"""
    new_data = f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
    return new_data