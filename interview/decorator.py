def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@retry(3)
def hello():
    print('Hello, World!')


if __name__ == '__main__':
    hello()
