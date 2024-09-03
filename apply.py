def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

def my_function(x, y):
    return x + y

result = my_function(3, 5)
print(f"Result: {result}")