#!python3

# Definindo um caractere
letra = 'P'

# Exibindo um caractere
print(letra)

# Identificando um determinado caractere
caractere = 'F'

print("O caractere ", caractere)
if caractere.isalnum():
  print("  É um número ou uma letra")

if caractere.isalpha():
  print("  É uma letra")

if caractere.isdecimal():
  print("  É um caractere decimal")

if caractere.isdigit():
  print("  É um digito")

if caractere.isidentifier():
  print("  É um identificador válido")

if caractere.islower():
  print("  É uma minúscula")

if caractere.isnumeric():
  print("  É um número")

if caractere.isprintable():
  print("  É um imprimivel")

if caractere.isspace():
  print("  É um espaço em branco")

if caractere.istitle():
  print("  É um titulo")

if caractere.isupper():
  print("  É uma letra maiúscula")
