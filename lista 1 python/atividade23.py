altura_pessoa = float(input("Digite sua altura (em metros): "))
sombra_pessoa = float(input("Digite o tamanho da sua sombra (em metros): "))
altura_predio = float(input("Digite o tamanho da sombra do prédio (em metros): "))
altura_predio = (altura_predio * altura_pessoa) / sombra_pessoa
print(f"A altura do prédio é de: {altura_predio} metros.")