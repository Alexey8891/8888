import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("") == ""


@pytest.mark.parametrize("date, expected",
                         [("2024-03-11T02:26:18.671407", "11.03.2024"),
                          ("2024-02-12T03:48:52.548921", "12.02.2024"),
                          ("2023-05-11T06:52:53.236585", "11.05.2023"),
                          ("2022-05-09T06:52:53.236585", "09.05.2022")])
def test_get_date(date, expected):
    assert get_date(date) == expected
