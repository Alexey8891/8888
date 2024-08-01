text_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(text_list: list, state: str = 'EXECUTED') -> list[str]:
    """Функция фильтрации операции по ключу 'state'."""
    new_list = []
    for text in text_list:
        if text.get('state') == state:
            new_list.append(text)
    return new_list


def sort_by_date(text_list: list[dict[str]], reverse: bool = True) -> list[dict[str,]]:
    """Функция сортирующая исходные данные по дате."""
    sorted_text_list = sorted(text_list, key=lambda text_list: text_list['date'], reverse=reverse)
    return sorted_text_list



print(filter_by_state(text_list, state='EXECUTED'))
print(sort_by_date(text_list))
