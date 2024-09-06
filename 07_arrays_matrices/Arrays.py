#!python3

# Declarando um vetor para números inteiros
numeros = []

# Atribuindo dados ao vetor
numeros.append(1)
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(5)

# Atribuindo dados ao vetor na declaração
pares = [ 0, 2, 4, 6, 8 ]

# Utilizando o tamanho do vetor
for i in range(0, len(pares)):
  print(pares[i])

# Mostrando os dados contidos no vetor
for num in pares:
  print(num)

# Armazenando textos em vetores
frutas = ["Uva", "Maçã", "Abacaxi", "Manga", "Banana"]

# Ordenando um vetor de textos
frutas.sort()
for fruta in frutas:
  print(fruta)