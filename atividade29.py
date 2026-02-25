Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.
preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.10
novo_preco = preco - desconto
print("O novo preço do produto com desconto é:", novo_preco)
