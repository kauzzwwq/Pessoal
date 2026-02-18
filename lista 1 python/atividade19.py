GALINHAS = float (input("Insira a quantidade de galinhas: "))
anel_chip = 3.50 
chip_alimento = 4.00
custo_galinha = anel_chip + (2 * chip_alimento)
print(f"O custo total para cada galinha é de: R$ {custo_galinha}")
custo_total = custo_galinha * GALINHAS
print(f"O custo total para as {GALINHAS} galinhas é de: R$ {custo_total}")

