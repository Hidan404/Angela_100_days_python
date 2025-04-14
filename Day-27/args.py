def soma(*args):
    """
    Função que soma todos os números passados como argumento.
    :param args: Números a serem somados.
    :return: Soma dos números.
    """
    total = [n for n in args]
    return sum(total)

def media(*args):
    """
    Função que calcula a média dos números passados como argumento.
    :param args: Números a serem calculados a média.
    :return: Média dos números.
    """
    return sum(args) / len(args)
def maior(*args):
    """
    Função que retorna o maior número passado como argumento.
    :param args: Números a serem comparados.
    :return: Maior número.
    """
    return max(args)
print(soma(1, 2, 3, 4, 5))  # Saída: 15



def alunos(**kwargs):
    """
    Função que imprime os nomes e notas dos alunos.
    :param kwargs: Nomes e notas dos alunos.
    """
    dicionario = {k: "A+" if v > 8 else "B-" for k, v in kwargs.items()}
    return dicionario

print(alunos(maria=9.5, joao=8.0, ana=10.0))  # Saída: Maria: 9.5, João: 8.0, Ana: 10.0