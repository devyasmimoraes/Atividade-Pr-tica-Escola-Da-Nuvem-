# 1 Área da Circunferência
pi = 3.14159265
raio = float(input("Digite o valor do raio: "))
area = pi * (raio ** 2)
print("A=%.4f" % area)
print()





# 2 Classificador de Idade
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")
print()




# 3 Calculadora de IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)




if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("Seu IMC é:", round(imc, 2))
print("Classificação:", classificacao)
print()



# 4 Conversor de Temperatura
print("=== Conversor de Temperatura ===")
temp = float(input("Digite a temperatura: "))
origem = input("Converter de (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

if origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    elif destino == "K":
        resultado = temp + 273.15
    else:
        resultado = temp
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    elif destino == "K":
        resultado = (temp - 32) * 5/9 + 273.15
    else:
        resultado = temp
elif origem == "K":
    if destino == "C":
        resultado = temp - 273.15
    elif destino == "F":
        resultado = (temp - 273.15) * 9/5 + 32
    else:
        resultado = temp
else:
    print("Unidade inválida!")
    resultado = None

if resultado is not None:
    print("Temperatura convertida:", round(resultado, 2), destino)
print()




# 5 Verificador de Ano Bissexto
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")
print()




# 6 Calculadora de Comissão
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas: "))

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print("Total a receber = R$ %.2f" % total_receber)
print()





# 7 - Calculadora da Média
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10
print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Nota do exame: "))
    print("Nota do exame:", nota_exame)
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % media_final)