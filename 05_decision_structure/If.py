#!python3

# Avaliando apenas o resultado positivo
# -------------------------------------
idade = 18
if (idade >= 18):
  print("Maior de idade")

# Avaliando o resultado positivo e negativo
# -----------------------------------------
idade = 17
if (idade >= 18):
  print("Maior de idade")
else:
  print("Menor de idade")


# Avaliando mais de uma situação
# ------------------------------
idade = 15
if (idade >= 18):
  print("Maior de idade")
elif (idade >= 16):
  print("Menor de idade e pode votar")
else:
  print("Menor de idade e não pode votar")
