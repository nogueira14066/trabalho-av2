def valor_com_imposto(taxa_imposto, custo):
    return  custo + (custo * taxa_imposto/100)
taxa_imposto = float(input("Taxa de imposto: "))
custo = float(input("Custo: "))

valor_com_imposto=valor_com_imposto(taxa_imposto, custo)

print(f"Valor com imposto: {valor_com_imposto}")