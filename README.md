# Мой проект:

Банковский

## Описание:

"Банковский Проект" - это серверная часть виджета банковских операций.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Alexey8891/Home-Work.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```


## Использование:

### **Для использования вам необходимо перейти в директорию src.**

**Для того чтобы замаскировать ваш счет или карту зайдите в masks.py**

- В фукции которая маскирует номер карты введите 16 значный код
- А функции которая маскирует счет введите 20-значный код
- Затем нажмите сочетание клавиш Shift+F10
- В диалоговом окне появиться ваш замаскированный счет или номер карты

**Для того чтобы замаскировать номер карты и счет. А так же получить корректную дату зайдите в widget.py**

- В функции "mask_account_card" введите данные в виде "Счет и 20-цифр" или "Название карты и 16-цифр"
- В функции "get_data" введите дату в формате "2018-07-11T02:26:18.671407"

**Для того чтобы получить все выполненные или не выполненные, а так же дату операций зайдите в processing.py**

- Нажмите сочетание клавиш Shift+F10

## Тестирование:

1. Произведено тестирование для модуля masks.py
- На правильность ввода
- На пустой ввод
2. Произведено тестирование для модуля widget.py
- На правильность вывода
- На пустой ввод
3. Произведено тестирование для модуля processing.py
- С помощью фикстуры для проверки правильности работы модуля

##  Покрытие тестами:
- src\__init__.py                0      0   100%
- src\masks.py                  11      2    82%
- src\processing.py             12      0   100%
- src\widget.py                 21      5    76%
- tests\__init__.py              0      0   100%
- tests\confest.py               5      0   100%
- tests\test_masks.py            8      1    88%
- tests\test_processing.py       8      0   100%
- tests\test_widget.py           8      0   100%


## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).