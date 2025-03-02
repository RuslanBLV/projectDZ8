from decorators import log
import logging

logger = logging.getLogger("mask")
file_handler = logging.FileHandler("logs.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


@log()
def get_mask_card_number(card_number: str, encoding='utf-8') -> str:
    """Поступает номер карты и маскируется '***'"""
    logger.info(f"Ввод данных: {card_number}")
    logger.info(f"Проверка номера карты")
    if len(card_number) != 16:
        logger.error(f"Неверный номер карты")
        return "wrong number"
    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.info(f"результат: {result}")
    return result


@log()
def get_mask_account(account_number: str) -> str:
    """Поступает номер счета и маскируется '***'"""
    logger.info(f"Ввод данных: {account_number}")
    logger.info(f"Проверка номера счета")
    if len(account_number) != 20:
        logger.error(f"Неверный номер счета")
        return "Incorrect account entered"
    result = f"**{account_number[-4:]}"
    logger.info(f"результат: {result}")
    return result


# print(get_mask_card_number("7000792289606361"))
