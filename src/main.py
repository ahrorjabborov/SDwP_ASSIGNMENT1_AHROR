import random
from task1 import decorator_1


@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)


@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


from task2 import decorator_2

@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


from task3 import decorator_3
function_times = []

@decorator_3
def fun_1(a, b):
    print(a, b)

@decorator_3
def fun_2(c, d = 5):
    print(c)
    for i in range(d):
        print(i)

@decorator_3
def fun_3(f, g = [1, 4, 5, 0, 23, 54, 3, 6]):
    print(f)
    g.sort()
    print(g)

@decorator_3
def fun_4(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


from task4 import decorator_4

@decorator_4
def fun_5(f, g = [1, 4, 5, 0, 23, 54, 3, 6]):
    print(f)
    g.sort()
    print(g[100])



@decorator_4
def fun_6(n=2, m=5):
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = n + "inf"



if __name__ == "__main__":

    #############   TASK 1 ####################

    func()
    funx()
    func()
    funx()
    func()



    #############   TASK 2 ####################

    funh(None, bar2="")



    #############   TASK 3 ####################

    fun_1("hello", "world")
    fun_2(5)
    fun_3(7)
    fun_4(None, bar2="")
    function_times = sorted(function_times, key=lambda  i: i['Time'])
    rank = 1
    print("PROGRAM | RANK | TIME ELAPSED\n")

    for item in function_times:
        item['Rank'] = rank
        print(item['Name'], "   ", item['Rank'], "  ", item['Time'])
        rank += 1

    # print(function_times)




    fun_5(3)
    fun_6()



    #############   TASK 4 ####################




