# 1 Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("=== Conversor de Moeda ===")
print("Valor em reais:", valor_reais)
print("Em dólares:", round(valor_dolar, 2))
print("Em euros:", round(valor_euro, 2))
print()





# 2 Calculadora de Desconto
produto = "Camiseta"
preco = 50.00
desconto = 20

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print("=== Calculadora de Desconto ===")
print("Produto:", produto)
print("Preço original: R$", preco)
print("Desconto:", desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))
print()





# 3 Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3

print("=== Média Escolar ===")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média:", round(media, 2))
print()




# 4 Consumo de Combustível
distancia = 300
combustivel = 25
consumo = distancia / combustivel

print("=== Consumo de Combustível ===")
print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "L")
print("Consumo médio:", round(consumo, 2), "km/L")
print()




# 5 Soma com entrada do usuário
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
X = A + B
print("X =", X)
print()





# 6 Salário por horas trabalhadas
numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))

salario = horas_trabalhadas * valor_por_hora

print("Número do funcionário =", numero_funcionario)
print("Salário = R$", round(salario, 2))
