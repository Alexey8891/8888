from decorators import (log)


@log()
def get_mask_card_number(card: str) -> str:
    '''Функия маскирует номер карты.'''
    if len(card) == 16:
        return f'{card[:4]} {card[4:6]}{'*' * 2} {'*' * 4} {card[12:]}'
    else:
        return ''


def get_mask_account(acc_number: str) -> str:
    """Функция возвращает маску счёта."""
    if len(acc_number) == 25:
        return f'{'*' * 2}{acc_number[-4:]}'
    else:
        return ''


if __name__ == '__main__':
    print(get_mask_card_number('7000792289606361'))
    print(get_mask_account('73654108430135874305'))

