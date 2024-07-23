from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime
from typing import Any


def mask_account_card(card_number: str) -> str:
    """Функия которая маскирует номер карты и счёта."""
    if "Счет" in card_number:
        mask_account = f"Счет {get_mask_account(card_number[:])}"
        return mask_account
    elif "Счет" not in card_number:
        card_mask = get_mask_card_number(card_number[-16:])
        mask = card_number.replace(card_number[-16:], card_mask)
        return mask





print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
