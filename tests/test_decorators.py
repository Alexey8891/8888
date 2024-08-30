from src.decorators import log
from src.masks import get_mask_card_number


def test_log(capsys):
    get_mask_card_number('7000792289606361')
    message = capsys.readouterr()
    assert message.out.strip() == 'get_mask_card_number ok'
def test_error_func(capsys):
    get_mask_card_number(1, 2)
    message = capsys.readouterr()
    assert message.out.strip() == 'get_mask_card_number error: get_mask_card_number() takes 1 positional argument but 2 were given  inputs:(1, 2), {}'


def test_write_file():
    @log("Test.txt")
    def summa(a, b):
        return a + b
    summa(1, 2)
    with open("Test.txt", "r") as file:
        e = "summa ok"
        assert e == file.read()