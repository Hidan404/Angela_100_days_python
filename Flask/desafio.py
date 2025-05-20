import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator():
    def decorator(function):
        def wrapper():
            start_time = time.time()
            function()
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Função {function.__name__} levou {total_time} segundos para rodar.")
        return wrapper
    return decorator
  

@speed_calc_decorator()
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator()
def slow_function():
    for i in range(10000000):
        i * i