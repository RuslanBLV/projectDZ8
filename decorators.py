
def log(filename=None):
    """Обрабатывает каждую функцию и пишет результат в файл .txt либо в консоль"""
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    my_file = open(filename, "a")
                    my_file.write(f"{func.__name__} ok: {result}\n")
                    my_file.close()
                else:
                    print(f"{func.__name__} ok: {result}\n")
            except Exception as error:
                if filename is not None:
                    my_file = open(filename, "a")
                    my_file.write(f"{func.__name__} error: {error}\n")
                    my_file.close()
                else:
                    print(f"{func.__name__} ok: {error}\n")
        return inner
    return wrapper


def log_generator(filename: str = None):
    """Обрабатывает каждую функцию и пишет результат в файл .txt либо в консоль"""
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    for i in result:
                        my_file = open(filename, "a")
                        yield my_file.write(f"{func.__name__} ok: {i}\n")
                        my_file.close()
                else:
                    for i in result:
                        yield f"{func.__name__} ok: {i}\n"
            except Exception as error:
                if filename is not None:
                        my_file = open(filename, "a")
                        my_file.write(f"{func.__name__} error: {error}\n")
                        my_file.close()
                else:
                    yield f"{func.__name__} error: {error}\n"
        return inner
    return wrapper







