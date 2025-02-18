from decorators import log

@log()
def get_mask_card_number(card_number: str, encoding='utf-8') -> str:
    """Поступает номер карты и маскируется '***'"""
    if len(card_number) != 16:
        return "wrong number"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

@log()
def get_mask_account(account_number: str) -> str:
    """Поступает номер счета и маскируется '***'"""
    if len(account_number) != 20:
        return "Incorrect account entered"
    return f"**{account_number[-4:]}"


