import time

def decorator_1(fun):
    def wrapper(*args):
        start = time.perf_counter()
        result = fun(*args)
        end = time.perf_counter()
        print(fun.__name__ + ' call ' + str(wrapper.counter) + ' executed in ' + str(end - start) + ' seconds\n')
        wrapper.counter += 1
        return result

    wrapper.counter = 1
    return wrapper
