from functools import wraps
def log(filename=None):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f'{func} ok')
                else:
                    with open(filename, 'w') as file:
                        file.write(f'{func} ok')
                return result
            except Exception as e:
                if filename is None:
                    print(f'{func} error: {e}  inputs:{args}, {kwargs}')
                else:
                    with open(filename, 'w') as file:
                        file.write(f'{func} error: {e}  inputs:{args}, {kwargs}')
        return wrapper
    return decor










