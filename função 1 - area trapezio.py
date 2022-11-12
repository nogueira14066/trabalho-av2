def calcular_area(bs_maior, bs_menor, altura):
  return((bs_maior+bs_menor)*altura)/2

bs_maior=float(input("Digite a base Maior: "))
bs_menor=float(input("Digite a base menor: "))
altura=float(input("Digite a altura: "))

trapezio=calcular_area(bs_maior, bs_menor, altura)

print(f"A altura do trapézio é: {trapezio}")
