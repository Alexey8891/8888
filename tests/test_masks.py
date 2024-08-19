from src.masks import get_mask_account, get_mask_card_number


def test_mask_account():
    assert get_mask_account("73654108430135874305") == ""


def test_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_mask_account_empty():
    assert get_mask_account('') == ''


def test_mask_card_number_empty():
    assert get_mask_card_number('') == ''
