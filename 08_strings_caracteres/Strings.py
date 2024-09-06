#!python3

# Declarando uma string
str = ""

# Preenchendo uma string
str = "Linguagem Python"

# Obtendo o tamanho da string
tamanho = len(str)
print(tamanho)

# Obtendo uma substring
substring = str[:5]
print(substring)

# Substituindo uma substring por outra substring
str = str.replace("Python", "PYTHON")
print(str)

# Substituindo todas substring por outra substring
str = "red;green;blue"
str = str.replace(";", ",")
print(str)

# Removendo substring
str = "81200-200"
str = str.replace("-", "")
print(str)

# Comparando strings
str1 = "Python"
str2 = "PYTHON"
if str1 == str2:
  print("São iguais")
else:
  print("Não são iguais")

# Verificando se a string é vazia
str = ""
if str:
  print("Não é vazia")
else:
  print("É vazia")

# Removendo espaços em branco
str = " Python "
str = str.strip()
print(str)

# Quebrando um string
str = "banana,abacate,abacaxi"
str = str.split(",")
print(str)
