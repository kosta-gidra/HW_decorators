from datetime import datetime


def logger(foo):
    def new_foo(*args, **kwargs):
        result = foo(*args, **kwargs)
        log_foo = f'{datetime.now()}; Name:{foo.__name__}; Args:{args}; Kwargs:{kwargs}; Result:{result}\n'
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(log_foo)
        return result
    return new_foo


def logger_path(path):
    def logger_p(foo):
        def new_foo(*args, **kwargs):
            result = foo(*args, **kwargs)
            log_foo = f'{datetime.now()}; Name:{foo.__name__}; Args:{args}; Kwargs:{kwargs}; Result:{result}\n'
            with open(path, 'a', encoding='utf-8') as file:
                file.write(log_foo)
            return result
        return new_foo
    return logger_p
