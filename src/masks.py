# маскировка номера карты
def get_mask_card_number(card_number: str) -> str:
    """Поступает номер карты и маскируется '***'"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


# маскировка номера счета
def get_mask_account(account_number: str) -> str:
    """Поступает номер счета и маскируется '***'"""
    return f"**{account_number[-4:]}"