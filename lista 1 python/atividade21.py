coca_lata = float(input("Insira a quantidade de coca-colas 350ml: "))
custo_lata = 350
coca_garrafa = float(input("Insira a quantidade de coca-colas 600ml: "))
custo_garrafa = 600
coca_litro = float(input("Insira a quantidade de coca-colas 2L: "))
custo_litro = 2000
litros_coca = (coca_lata * custo_lata) + (coca_garrafa * custo_garrafa) + (coca_litro * custo_litro)
print(f"A quantidade total de coca-cola em litros é de: {litros_coca} ml.")
