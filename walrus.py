def total() -> int:
    total_n = 0
    while (valor := int(input("digite um numero: "))) != 0:
        total_n+= valor

    return total_n   

print(total()) 

tuplas = (tuplas := 5, 6)
print(tuplas)

numeros = [[(q := n ** 2), q * 2, q * 3] for n in range(1,5)]
print(numeros)

a = "  "
texto = b.lower() if (b := a.strip()) else "-" * 5


n = [1,2,3]
texto_formatado = f"{n} tem {(tamanho := len(a))} elementos e soma de {(soma := sum(n))} e media de {soma / tamanho}"
print(texto_formatado)