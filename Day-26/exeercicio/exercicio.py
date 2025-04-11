numeros1 = []
numeros2 = []
with open("Day-26/exeercicio/file1.txt", "r") as f1:
    numeros = [int(l.strip()) for l in f1]
    numeros1 = [n for n in numeros]

with open("Day-26/exeercicio/file2.txt", "r") as f2:
    numeros = [int(l.strip()) for l in f2]
    numeros2 = [n for n in numeros]


result = list(set(numeros1) & set(numeros2))

print(result)