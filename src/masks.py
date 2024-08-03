def get_mask_card_number(card: str) -> str:
    """Функция маскирует номер карты."""
    if len(card) == 16:
        return f'{card[:4]} {card[4:6]}{'*' * 2} {'*' * 4} {card[12:]}'
    else:
        return ''


def get_mask_account(acc_number: str) -> str:
    """Функция возвращает маску счёта."""
    if len(acc_number) == 20:
        return f'{'*' * 2}{acc_number[-4:]}'
    else:
        return ''


def get_mask_account_long(acc_number: str) -> str:
    """Функция возвращает маску счёта."""
    if len(acc_number) == 25:
        return f'{'*' * 2}{acc_number[-4:]}'
    else:
        return ''
