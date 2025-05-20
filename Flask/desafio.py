import time
tempo_atual = time.time()
print(tempo_atual) # segundos desde 1º de janeiro de 1970 

# Escreva seu código abaixo 👇

def decorador_calculo_velocidade():
    def decorador(funcao):
        def wrapper():
            tempo_inicio = time.time()
            funcao()
            tempo_fim = time.time()
            tempo_total = tempo_fim - tempo_inicio
            print(f"Velocidade de execução de {funcao.__name__}: {tempo_total}s")
        return wrapper
    return decorador
  

@decorador_calculo_velocidade()
def funcao_rapida():
    for i in range(1000000):
        i * i


@decorador_calculo_velocidade()
def funcao_lenta():
    for i in range(10000000):
        i * i

 
funcao_rapida()
funcao_lenta()      