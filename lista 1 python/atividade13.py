inteiro = int(input("Insira um número inteiro de 3 digitos: "))
centena = inteiro // 100
resto = inteiro % 100
dezena = resto // 10
unidade = resto % 10
print("A centena é: ", centena)
print("A dezena é: ", dezena)
print("A unidade é: ", unidade)
