import time


def decorator_4(fun):
    def wrapper(*args, **kwargs):
        try:
            result = fun(*args, **kwargs)
        except Exception as exc:
            result = ""
            with open("log_file.txt", 'a') as file:
                file.write("Exception: " + str(exc) + "\n")
                file.write("Function: " + fun.__name__ + " call " + str(wrapper.counter) + "\n")
                file.write("Timestamp: " + str(time.time()) + "\n\n")

        return result


    wrapper.counter = 1
    return wrapper