# TODO: Create the logging_decorator() function 👇
def logging_decorator(funcao):
    def wrapper(*args):
        args_str = ",".join(str(arg) for arg in args)
        print(f"You called a_function({args_str})")
        resultado = funcao(*args)
        print(f"It returned: {resultado}")
        return resultado
    return wrapper


# TODO: Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)