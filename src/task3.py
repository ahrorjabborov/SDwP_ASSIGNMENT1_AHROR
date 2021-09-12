import contextlib
import io
import time
import inspect

class decorator_3:

    def __init__(self, fun):
        self.fun = fun
        self.counter = 1
        self.function_times = fun.__globals__["function_times"]

    def __call__(self, *args, **kwargs):

        with contextlib.redirect_stdout(io.StringIO()) as func:
            start = time.perf_counter()
            result = self.fun(*args, **kwargs)
            end = time.perf_counter()
        output = func.getvalue()
        with open('task3text.txt', 'a') as file:
            file.write(self.fun.__name__ + " call " + str(self.counter) + " executed in " + str(end - start) + " seconds")
            self.function_times.append({"Name" : self.fun.__name__, "Time": end - start})
            file.write("\nName: " + self.fun.__name__)
            file.write("\nType: " + str(type(self.fun)))
            file.write("\nSign: " + str(inspect.signature(self.fun)))
            file.write("\nArgs: positional " + str(self.fun.__defaults__))
            file.write("\n      keyworded " + str(self.fun.__kwdefaults__))
            file.write("\nDoc: " + str(self.fun.__doc__))
            file.write("\nSource: " + str(inspect.getsource(self.fun)))
            file.write("\nOutput: " + output + "\n\n\n")
            print(output)
        self.counter += 1
        return result

