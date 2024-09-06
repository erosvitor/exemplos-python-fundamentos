#!python3

marcas_veiculos = ["Fiat", "Mercedes", "Ford", "BMW"]

# Obter quantidade de elementos
print(len(marcas_veiculos))

# Verificar se um determinado item existe na lista
print("Chevrolet" in marcas_veiculos)

# Adicionar item no final da lista
marcas_veiculos.append("Chevrolet")
print(marcas_veiculos)

# Inserir item numa determinada posição da lista
marcas_veiculos.insert(1, "Ferrari")
print(marcas_veiculos)

# Ordenar a lista em ordem ascendente
marcas_veiculos.sort()
print(marcas_veiculos)

# Ordenar a lista em ordem descendente
marcas_veiculos.reverse()
print(marcas_veiculos)

# Retirar o último elemento da lista
ultimo_elemento = marcas_veiculos.pop()
print(ultimo_elemento)
print(marcas_veiculos)

# Remover todos os elementos da lista
marcas_veiculos.clear()