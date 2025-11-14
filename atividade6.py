import datetime
import string

# 1. Função da Calculadora de Gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
    float: O valor da gorjeta calculada.
    """
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0  # Gorjeta não pode ser negativa
        
    valor_gorjeta = (valor_conta * porcentagem_gorjeta) / 100
    return valor_gorjeta

# 2. Função de Verificação de Palíndromo
def eh_palindromo(frase):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços, pontuação e maiúsculas/minúsculas.

    Parâmetros:
    frase (str): A palavra ou frase a ser verificada.

    Retorna:
    str: "Sim" se for um palíndromo, "Não" caso contrário.
    """
    # Remove pontuação e espaços, e converte para minúsculas
    # Caracteres de pontuação a serem removidos
    pontuacao = string.punctuation + " " + "!" + "?" + "." + "," + ";" + ":"
    
    # Cria a string limpa: minúscula e sem pontuação/espaços
    texto_limpo = "".join(
        char.lower() for char in frase if char not in pontuacao
    )
    
    # Compara a string limpa com sua versão invertida
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# 3. Programa da Calculadora de Desconto
def executar_calculadora_desconto():
    """
    Função principal para rodar o programa de cálculo de desconto.
    Pede ao usuário o preço e o desconto, e exibe o preço final.
    """
    print("--- Calculadora de Desconto ---")
    try:
        # Permite que o usuário informe o preço e o desconto
        preco_original = float(input("Digite o preço original do produto (R$): "))
        percentual_desconto = float(input("Digite o percentual de desconto (ex: 15 para 15%): "))

        if preco_original < 0 or percentual_desconto < 0:
            print("Valores não podem ser negativos.")
            return

        # Utiliza operações matemáticas para calcular
        valor_desconto = (preco_original * percentual_desconto) / 100
        preco_final = preco_original - valor_desconto

        # Exibe o preço final com duas casas decimais
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto de {percentual_desconto}%: R$ {valor_desconto:.2f}")
        print(f"Preço final com desconto: R$ {preco_final:.2f}")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# 4. Função de Cálculo de Idade em Dias
def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade aproximada de uma pessoa em dias, baseada no ano de nascimento.
    Nota: Esta é uma aproximação que não considera anos bissextos.

    Parâmetros:
    ano_nascimento (int): O ano de nascimento.

    Retorna:
    int: A idade aproximada em dias.
    """
    try:
        ano_atual = datetime.datetime.now().year
        
        if ano_nascimento > ano_atual:
            return 0 # Ano de nascimento não pode ser no futuro

        idade_em_anos = ano_atual - ano_nascimento
        idade_em_dias = idade_em_anos * 365
        
        # Uma simples (mas não perfeita) adição de anos bissextos
        # Conta quantos anos bissextos houveram aproximadamente
        num_bissextos = (idade_em_anos // 4)
        idade_em_dias += num_bissextos

        return idade_em_dias
        
    except Exception as e:
        print(f"Erro ao calcular idade: {e}")
        return 0

# --- Bloco de Execução Principal ---
# Este bloco só será executado se você rodar este arquivo diretamente.
if __name__ == "__main__":
    
    print("=============================================")
    print("EXECUTANDO DEMONSTRAÇÕES DAS FUNÇÕES")
    print("=============================================\n")

    # 1. Testando a Calculadora de Gorjeta
    print("--- Teste: Calculadora de Gorjeta ---")
    conta = 150.0
    percentual = 20.0
    gorjeta = calcular_gorjeta(conta, percentual)
    print(f"Conta: R$ {conta:.2f}, Percentual: {percentual}%")
    print(f"Valor da Gorjeta: R$ {gorjeta:.2f}\n")

    # 2. Testando o Verificador de Palíndromo
    print("--- Teste: Verificador de Palíndromo ---")
    frase1 = "Anotaram a data da maratona"
    frase2 = "Python não é palíndromo"
    print(f"'{frase1}': {eh_palindromo(frase1)}")
    print(f"'{frase2}': {eh_palindromo(frase2)}\n")

    # 4. Testando a Idade em Dias
    # (O programa 3 será executado a seguir)
    print("--- Teste: Calculadora de Idade em Dias ---")
    ano = 1990
    dias = calcular_idade_em_dias(ano)
    print(f"Quem nasceu em {ano} tem aproximadamente {dias} dias de vida.\n")

    # 3. Executando a Calculadora de Desconto
    # Esta função é interativa e pedirá sua entrada
    executar_calculadora_desconto()