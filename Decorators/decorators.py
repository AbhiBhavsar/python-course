import time

def runTime(function):
    def wrapper_function():
        current_time = time.time()
        function()
        print(current_time)
    return wrapper_function()


@runTime
def speed_calc_decorator():
    pass

@runTime
def fast_function():
    for i in range(10000000):
        i * i

@runTime
def slow_function():
    for i in range(100000000):
        i * i
