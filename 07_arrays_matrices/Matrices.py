#!python3

# Declarando uma matriz para números inteiros
numeros = []

# Atribuindo dados para a matriz
numeros.append([1, 1])
numeros.append([2, 3])
print(numeros)

# Atribuindo dados para a matriz na declaração
coordenadas = [ [ 2, 2 ], [ 2, 8 ], [ 5, 2 ], [ 3, 2 ] ]

# Mostrando os dados contidos na matriz
for linha in coordenadas:
    for item in linha:
        print(item)
