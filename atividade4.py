# 1 Calculadora com tratamento de erros
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            print("Operação inválida! Tente novamente.\n")
            continue

        print("Resultado:", resultado)
        break

    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.\n")
print()





# 2 Registro de notas da turma
notas = []
while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'fim'.")
print()

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("Média da turma:", round(media, 2))
else:
    print("Nenhuma nota válida foi inserida.")
print()





# 3 Verificador de senha forte
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca! Deve ter pelo menos 8 caracteres.\n")
        continue

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("Senha fraca! Deve conter pelo menos um número.\n")
        continue

    print("Senha forte! ✅")
    break
print()






# 4 Verificador de números pares e ímpares
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(numero, "é par.")
            pares += 1
        else:
            print(numero, "é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.\n")

print()
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
