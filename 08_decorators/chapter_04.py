from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            return f"From Cache: {cache[key]}"

        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return f"Computed: {result}"

    return wrapper


@cache_results
def multiply(a: int, b: int) -> int:
    return a * b

multiply(3,5)