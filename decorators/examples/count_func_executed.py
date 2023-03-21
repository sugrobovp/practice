def count_decorator(func):

    def wrapped(*args, **kwargs):
        wrapped.num_executions += 1
        return func(*args, **kwargs)

    wrapped.num_executions = 0

    return wrapped


@count_decorator
def some_func():
    pass


some_func()
some_func()

print(some_func.num_executions) # 2