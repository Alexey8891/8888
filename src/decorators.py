from functools import wraps

def log(filename=None):
    "Декоратор для логирования функции."
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            "Автоматически логирует начало и конец выполнения функции и её результаты или возникшие ошибки."
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f'{func.__name__} ok')
                else:
                    with open(filename, 'w') as file:
                        file.write(f'{func.__name__} ok')
                return result
            except Exception as e:
                if filename is None:
                    print(f'{func.__name__} error: {e}  inputs:{args}, {kwargs}')
                else:
                    with open(filename, 'w') as file:
                        file.write(f'{func.__name__} error: {e}  inputs:{args}, {kwargs}')
        return wrapper
    return decor










