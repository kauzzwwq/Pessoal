Horast =  (input("Insira a quantidade de horas trabalhadas: "))
horase =  (input("Insira a quantidade de horas extras trabalhadas: "))

salarioB = (float(Horast) * 10) + (float(horase) * 15)
print(f"O salário Bruto do funcionário é de: R$ {salarioB}")
desconto = salarioB * 0.10
salarioL = salarioB - desconto

print(f"O salário líquido do funcionário é de: R$ {salarioL}")    
