from datetime import datetime

def logger(filename_path):
    def log_decorator(old_function):
        def new_function(*args, **kwargs):
            start = datetime.now()
            result = old_function(*args, **kwargs)
            f = open(filename_path, 'a')
            f.write(f'\n{start}, {old_function.__name__}, {args}, {kwargs}, {result}')
            f.close()
            return result
        return new_function
    return log_decorator