from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(fixture_by_currency):
    assert next(filter_by_currency(fixture_by_currency, "USD")) == {'id': 939719570, 'state': 'EXECUTED',
                                                                    'date': '2018-06-30T02:08:58.425572',
                                                                    'operationAmount': {'amount': '9824.07',
                                                                                        'currency': {'name': 'USD',
                                                                                                     'code': 'USD'}},
                                                                    'description': 'Перевод организации',
                                                                    'from': 'Счет 75106830613657916952',
                                                                    'to': 'Счет 11776614605963066702'}


def test_transaction_descriptions(fixture_by_currency):
    assert next(transaction_descriptions(fixture_by_currency)) == "Перевод организации"


def test_card_number_generator():
    assert next(card_number_generator(1, 2)) == "0000 0000 0000 0001"
