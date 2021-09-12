import time
import inspect
import contextlib
import io
def decorator_2(fun):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fun(*args)
        end = time.perf_counter()
        print(fun.__name__ + " call " + str(wrapper.counter) + " executed in " + str(end - start) + " seconds")
        wrapper.counter += 1
        print("Name: " + fun.__name__ )
        print("Type: " + str(type(fun)))
        print("Sign: " + str(inspect.signature(fun)))
        print("Args: positional " + str(locals()['args'])) # fun.__defaults__ didn't work properly
        print("      keyworded " + str(locals()['kwargs'])) # fun.__kwdefaults__ didn't work properly
        print("Doc: " + str(fun.__doc__))
        print("Source: " + str(inspect.getsource(fun)))
        with contextlib.redirect_stdout(io.StringIO()) as func:
            fun(*args, **kwargs)
        output = func.getvalue()
        print("Output: " + output)

        return result

    wrapper.counter = 1
    return wrapper

