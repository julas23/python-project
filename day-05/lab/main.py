import time

def timeit(unit='seconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Timeit decorator start for {func.__name__}')
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if unit == 'seconds':
                print(f'Time taken to run {func.__name__}: {end_time - start_time} seconds')
            elif unit == 'milliseconds':
                print(f'Time taken to run {func.__name__}: {(end_time - start_time) * 1000} milliseconds')
            else:
                raise NotImplementedError(f'Unit {unit} is not supported')
            print(f'Timeit decorator end for {func.__name__}')
            return result
        return wrapper
    return decorator

def logit(func):
    def wrapper(*args, **kwargs):
        print(f'Logit decorator start for {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Arguments: {args}, {kwargs}')
        print(f'Return value: {result}')
        print(f'Logit decorator end for {func.__name__}')
        return result
    return wrapper

@timeit()
def generate_numbers():
    for i in range(1, 11):
        yield i

@logit
@timeit(unit='milliseconds')
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in generate_numbers():
    print(number)

for number in generate_fibonacci(10):
    print(number)