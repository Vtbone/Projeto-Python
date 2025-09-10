# Lista Completa de 69 Exercícios Python

# Importações necessárias para os exercícios
import random      # Para números aleatórios (exercício 57, 64, 68)
import re          # Para validação de email e nome (exercício 68)
from datetime import datetime  # Para validação de data (exercício 68)

# ===== EXERCÍCIOS 1-10: ESTRUTURAS CONDICIONAIS BÁSICAS =====

def exercicio_01():
    """Exercício 1: Converter número (1-3) para seu nome por extenso"""
    numero = int(input("Digite um número de 1 a 3: "))
    if numero == 1:
        print("um")
    elif numero == 2:
        print("dois")
    elif numero == 3:
        print("três")
    else:
        print("Número inválido!")

def exercicio_02():
    """Exercício 2: Verificar se um número é maior que 10"""
    numero = int(input("Digite um número: "))
    if numero > 10:
        print("O número é maior que 10")
    else:
        print("O número não é maior que 10")

def exercicio_03():
    """Exercício 3: Converter número (1-7) para dia da semana"""
    dia = int(input("Digite um número de 1 a 7 para o dia da semana: "))
    dias = {1: "Segunda-feira", 2: "Terça-feira", 3: "Quarta-feira", 
            4: "Quinta-feira", 5: "Sexta-feira", 6: "Sábado", 7: "Domingo"}
    print(dias.get(dia, "Número inválido!"))

def exercicio_04():
    """Exercício 4: Exibir mensagem baseada na cor escolhida"""
    cor = input("Digite uma cor (vermelho, verde, azul): ").lower()
    if cor == "vermelho":
        print("Cor vibrante e energética!")
    elif cor == "verde":
        print("Cor da natureza!")
    elif cor == "azul":
        print("Cor calma e serena!")
    else:
        print("Cor não reconhecida!")

def exercicio_05():
    """Exercício 5: Verificar se dois números são ambos pares"""
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Ambos os números são pares")
    else:
        print("Pelo menos um dos números não é par")

def exercicio_06():
    """Exercício 6: Calculadora simples com as quatro operações básicas"""
    operacao = input("Digite uma operação (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if operacao == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacao == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacao == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacao == "/":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Operação inválida!")

def exercicio_07():
    """Exercício 7: Classificar nota como Baixa, Média ou Alta"""
    nota = float(input("Digite uma nota de 0 a 10: "))
    if 0 <= nota < 4:
        print("Baixa")
    elif 4 <= nota < 7:
        print("Média")
    elif 7 <= nota <= 10:
        print("Alta")
    else:
        print("Nota inválida!")

def exercicio_08():
    """Exercício 8: Verificar e exibir estado civil do usuário"""
    estado = input("Digite seu estado civil (solteiro, casado, divorciado, viúvo): ").lower()
    estados_validos = ["solteiro", "casado", "divorciado", "viúvo"]
    if estado in estados_validos:
        print(f"Você é {estado}(a)")
    else:
        print("Estado civil não reconhecido!")

def exercicio_09():
    """Exercício 9: Verificar se um número é par ou ímpar"""
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

def exercicio_10():
    """Exercício 10: Verificar se pessoa é maior ou menor de idade"""
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

# ===== EXERCÍCIOS 11-20: ESTRUTURAS CONDICIONAIS INTERMEDIÁRIAS =====

def exercicio_11():
    """Exercício 11: Exibir mensagem de boas-vindas personalizada"""
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Seja bem-vindo!")

def exercicio_12():
    """Exercício 12: Exibir velocidade média baseada no modo de transporte"""
    transporte = input("Escolha um modo de transporte (carro, bicicleta, a pé): ").lower()
    if transporte == "carro":
        print("Velocidade média: 60 km/h")
    elif transporte == "bicicleta":
        print("Velocidade média: 15 km/h")
    elif transporte == "a pé":
        print("Velocidade média: 5 km/h")
    else:
        print("Modo de transporte não reconhecido!")

def exercicio_13():
    """Exercício 13: Determinar estação do ano baseada no mês (Hemisfério Sul)"""
    mes = int(input("Digite um mês (1-12): "))
    if mes in [12, 1, 2]:
        print("Verão")
    elif mes in [3, 4, 5]:
        print("Outono")
    elif mes in [6, 7, 8]:
        print("Inverno")
    elif mes in [9, 10, 11]:
        print("Primavera")
    else:
        print("Mês inválido!")

def exercicio_14():
    """Exercício 14: Verificar se a soma de dois números é maior que 100"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    if soma > 100:
        print(f"A soma ({soma}) é maior que 100")
    else:
        print(f"A soma ({soma}) não é maior que 100")

def exercicio_15():
    """Exercício 15: Verificar se pessoa é adolescente (13-17 anos)"""
    idade = int(input("Digite sua idade: "))
    if 13 <= idade <= 17:
        print("Você é adolescente")
    else:
        print("Você não é adolescente")

def exercicio_16():
    """Exercício 16: Exibir preço do combustível baseado no tipo"""
    combustivel = input("Digite o tipo de combustível (gasolina, etanol, diesel): ").lower()
    if combustivel == "gasolina":
        print("Preço: R$ 5.50 por litro")
    elif combustivel == "etanol":
        print("Preço: R$ 3.80 por litro")
    elif combustivel == "diesel":
        print("Preço: R$ 4.20 por litro")
    else:
        print("Tipo de combustível não reconhecido!")

def exercicio_17():
    """Exercício 17: Realizar todas as operações matemáticas básicas"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"Soma: {num1 + num2}")
    print(f"Subtração: {num1 - num2}")
    print(f"Multiplicação: {num1 * num2}")
    if num2 != 0:
        print(f"Divisão: {num1 / num2}")
    else:
        print("Divisão: Não é possível dividir por zero")

def exercicio_18():
    """Exercício 18: Verificar se três números são todos positivos"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    if num1 > 0 and num2 > 0 and num3 > 0:
        print("Todos os números são positivos")
    else:
        print("Nem todos os números são positivos")

def exercicio_19():
    """Exercício 19: Verificar se a fruta digitada é uma maçã"""
    fruta = input("Digite o nome de uma fruta: ").lower()
    if fruta == "maçã" or fruta == "maca":
        print("É uma maçã!")
    else:
        print("Não é uma maçã")

def exercicio_20():
    """Exercício 20: Converter temperatura de Celsius para Fahrenheit"""
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

# ===== EXERCÍCIOS 21-40: ESTRUTURAS CONDICIONAIS AVANÇADAS =====

def exercicio_21():
    """Exercício 21: Comparar número com 10 (maior, menor ou igual)"""
    numero = float(input("Digite um número: "))
    if numero > 10:
        print("O número é maior que 10")
    elif numero < 10:
        print("O número é menor que 10")
    else:
        print("O número é igual a 10")

def exercicio_22():
    """Exercício 22: Verificar se o primeiro número é maior que o segundo"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num1 > num2:
        print("O primeiro número é maior que o segundo")
    else:
        print("O primeiro número não é maior que o segundo")

def exercicio_23():
    """Exercício 23: Verificar se a palavra digitada é 'Python'"""
    palavra = input("Digite uma palavra: ")
    if palavra.lower() == "python":
        print("A palavra é Python!")
    else:
        print("A palavra não é Python")

def exercicio_24():
    """Exercício 24: Verificar se a cidade é a capital do Brasil"""
    cidade = input("Digite o nome de uma cidade: ").lower()
    if cidade == "brasília" or cidade == "brasilia":
        print("É a capital do Brasil!")
    else:
        print("Não é a capital do Brasil")

def exercicio_25():
    """Exercício 25: Verificar se número está no intervalo de 10 a 15"""
    numero = int(input("Digite um número de 0 a 20: "))
    if 10 <= numero <= 15:
        print("O número está entre 10 e 15")
    else:
        print("O número não está entre 10 e 15")

def exercicio_26():
    """Exercício 26: Verificar se ambos os números são múltiplos de 5"""
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 % 5 == 0 and num2 % 5 == 0:
        print("Ambos os números são múltiplos de 5")
    else:
        print("Nem todos os números são múltiplos de 5")

def exercicio_27():
    """Exercício 27: Encontrar o maior de três números"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    maior = max(num1, num2, num3)
    print(f"O maior número é: {maior}")

def exercicio_28():
    """Exercício 28: Verificar se uma palavra tem mais de 5 letras"""
    palavra = input("Digite uma palavra: ")
    if len(palavra) > 5:
        print("A palavra tem mais de 5 letras")
    else:
        print("A palavra não tem mais de 5 letras")

def exercicio_29():
    """Exercício 29: Verificar se um número é múltiplo de 3"""
    numero = int(input("Digite um número: "))
    if numero % 3 == 0:
        print("O número é múltiplo de 3")
    else:
        print("O número não é múltiplo de 3")

def exercicio_30():
    """Exercício 30: Verificar se pessoa pode votar (16+ anos no Brasil)"""
    idade = int(input("Digite sua idade: "))
    if idade >= 16:
        print("Você pode votar")
    else:
        print("Você não pode votar")

def exercicio_31():
    """Exercício 31: Verificar se número de 1 a 5 é igual a 3"""
    numero = int(input("Digite um número de 1 a 5: "))
    if numero == 3:
        print("O número é igual a 3")
    else:
        print("O número não é igual a 3")

def exercicio_33():
    """Exercício 33: Calcular desconto de 10% em um produto"""
    valor = float(input("Digite o valor do produto: R$ "))
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f"Valor com 10% de desconto: R$ {valor_final:.2f}")

def exercicio_34():
    """Exercício 34: Classificar número como positivo, negativo ou zero"""
    numero = float(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")

def exercicio_35():
    """Exercício 35: Verificar se a multiplicação de dois números é igual a 20"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if (num1 * num2) == 20:
        print("A multiplicação é igual a 20")
    else:
        print("A multiplicação não é igual a 20")

def exercicio_36():
    """Exercício 36: Converter número (1-12) para nome do mês"""
    numero = int(input("Digite um número de 1 a 12: "))
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    print(meses.get(numero, "Número inválido!"))

def exercicio_37():
    """Exercício 37: Verificar se número é múltiplo de 2 ou de 5"""
    numero = int(input("Digite um número: "))
    if numero % 2 == 0 or numero % 5 == 0:
        print("O número é múltiplo de 2 ou de 5")
    else:
        print("O número não é múltiplo de 2 nem de 5")

def exercicio_38():
    """Exercício 38: Verificar se altura é maior que 1,75m"""
    altura = float(input("Digite sua altura em metros: "))
    if altura > 1.75:
        print("Sua altura é maior que 1,75m")
    else:
        print("Sua altura não é maior que 1,75m")

def exercicio_39():
    """Exercício 39: Verificar se a senha digitada é '1234'"""
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("Senha correta!")
    else:
        print("Senha incorreta!")

def exercicio_40():
    """Exercício 40: Verificar se três números são todos iguais"""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    if num1 == num2 == num3:
        print("Todos os números são iguais")
    else:
        print("Os números não são todos iguais")

# ===== EXERCÍCIOS 41-50: ESTRUTURAS DE REPETIÇÃO (FOR) =====

def exercicio_41():
    """Exercício 41: Exibir números de 1 até o número informado"""
    numero = int(input("Digite um número inteiro positivo: "))
    if numero > 0:
        for i in range(1, numero + 1):
            print(i)
    else:
        print("Por favor, digite um número positivo")

def exercicio_42():
    """Exercício 42: Somar 5 números inteiros fornecidos pelo usuário"""
    soma = 0
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número: "))
        soma += numero
    print(f"A soma dos números é: {soma}")

def exercicio_43():
    """Exercício 43: Repetir uma mensagem N vezes usando for"""
    vezes = int(input("Quantas vezes deseja exibir a mensagem? "))
    mensagem = input("Digite a mensagem: ")
    for i in range(vezes):
        print(f"{i+1}. {mensagem}")

def exercicio_44():
    """Exercício 44: Receber 10 números e exibir apenas os pares"""
    print("Digite 10 números:")
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        if numero % 2 == 0:
            print(f"Número par: {numero}")

def exercicio_45():
    """Exercício 45: Encontrar o maior de 5 números"""
    maior = float('-inf')
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        if numero > maior:
            maior = numero
    print(f"O maior número é: {maior}")

def exercicio_46():
    """Exercício 46: Calcular a média de 10 números"""
    soma = 0
    for i in range(10):
        numero = float(input(f"Digite o {i+1}º número: "))
        soma += numero
    media = soma / 10
    print(f"A média dos números é: {media:.2f}")

def exercicio_47():
    """Exercício 47: Exibir a tabuada de um número de 1 a 10"""
    numero = int(input("Digite um número para ver sua tabuada: "))
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def exercicio_48():
    """Exercício 48: Exibir cada letra de uma palavra em linha separada"""
    palavra = input("Digite uma palavra: ")
    print("Letras da palavra:")
    for letra in palavra:
        print(letra)

def exercicio_49():
    """Exercício 49: Contar quantos de 7 números são maiores que 10"""
    contador = 0
    for i in range(7):
        numero = float(input(f"Digite o {i+1}º número: "))
        if numero > 10:
            contador += 1
    print(f"Quantidade de números maiores que 10: {contador}")

def exercicio_50():
    """Exercício 50: Exibir números de forma decrescente até 1"""
    numero = int(input("Digite um número: "))
    print(f"Contagem regressiva de {numero} até 1:")
    for i in range(numero, 0, -1):
        print(i)

# ===== EXERCÍCIOS 51-60: ESTRUTURAS DE REPETIÇÃO (WHILE) =====

def exercicio_51():
    """Exercício 51: Somar números até que o usuário digite 0"""
    soma = 0
    while True:
        numero = float(input("Digite um número (0 para parar): "))
        if numero == 0:
            break
        soma += numero
    print(f"A soma total é: {soma}")

def exercicio_52():
    """Exercício 52: Pedir senha até que o usuário acerte"""
    senha_correta = "1234"
    while True:
        senha = input("Digite a senha: ")
        if senha == senha_correta:
            print("Senha correta! Acesso liberado.")
            break
        else:
            print("Senha incorreta! Tente novamente.")

def exercicio_53():
    """Exercício 53: Fazer contagem regressiva até 1"""
    numero = int(input("Digite um número para contagem regressiva: "))
    while numero >= 1:
        print(numero)
        numero -= 1

def exercicio_54():
    """Exercício 54: Coletar números até que um negativo seja digitado"""
    print("Digite números (um número negativo para parar):")
    while True:
        numero = float(input("Digite um número: "))
        if numero < 0:
            print("Número negativo inserido. Parando...")
            break

def exercicio_55():
    """Exercício 55: Solicitar número até que seja maior que 100"""
    while True:
        numero = int(input("Digite um número maior que 100: "))
        if numero > 100:
            print(f"Perfeito! Você digitou {numero}")
            break
        else:
            print("O número deve ser maior que 100. Tente novamente.")

def exercicio_56():
    """Exercício 56: Exibir mensagem N vezes usando while"""
    vezes = int(input("Quantas vezes quer exibir a mensagem? "))
    mensagem = input("Digite a mensagem: ")
    contador = 0
    while contador < vezes:
        print(f"{contador + 1}. {mensagem}")
        contador += 1

def exercicio_57():
    """Exercício 57: Jogo de adivinhação de número de 1 a 10"""
    numero_secreto = random.randint(1, 10)
    print("Tente adivinhar o número secreto entre 1 e 10!")
    while True:
        palpite = int(input("Digite seu palpite: "))
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        else:
            print("Errou! Tente novamente.")

def exercicio_58():
    """Exercício 58: Coletar palavras até que o usuário digite 'sair'"""
    palavras = []
    while True:
        palavra = input("Digite uma palavra ('sair' para parar): ")
        if palavra.lower() == "sair":
            break
        palavras.append(palavra)
    print(f"Palavras digitadas: {palavras}")

def exercicio_59():
    """Exercício 59: Pedir números até que o primeiro seja maior que o segundo"""
    while True:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num1 > num2:
            print(f"Perfeito! {num1} é maior que {num2}")
            break
        else:
            print("O primeiro número deve ser maior que o segundo. Tente novamente.")

def exercicio_60():
    """Exercício 60: Exibir todos os divisores de um número usando while"""
    numero = int(input("Digite um número para ver seus divisores: "))
    print(f"Divisores de {numero}:")
    divisor = 1
    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
        divisor += 1

# ===== EXERCÍCIOS 61-65: LISTAS BÁSICAS =====

def exercicio_61():
    """Exercício 61: Criar lista de 1 a 5 e imprimir cada número"""
    numeros = [1, 2, 3, 4, 5]
    print("Números da lista:")
    for numero in numeros:
        print(numero)

def exercicio_62():
    """Exercício 62: Solicitar 3 nomes e armazenar em lista"""
    nomes = []
    for i in range(3):
        nome = input(f"Digite o {i+1}º nome: ")
        nomes.append(nome)
    print(f"\nLista de nomes: {nomes}")

def exercicio_63():
    """Exercício 63: Coletar 5 números em lista e calcular soma"""
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    soma = sum(numeros)
    print(f"A soma dos números é: {soma}")

def exercicio_64():
    """Exercício 64: Criar lista com números aleatórios e filtrar múltiplos de 3"""
    numeros = [random.randint(1, 50) for _ in range(10)]
    multiplos_de_3 = [num for num in numeros if num % 3 == 0]
    print(f"Lista original: {numeros}")
    print(f"Múltiplos de 3: {multiplos_de_3}")

def exercicio_65():
    """Exercício 65: Coletar 5 números e encontrar maior e menor"""
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")

# ===== EXERCÍCIOS 66-69: PROJETOS ESPECIAIS =====

def exercicio_66():
    """Exercício 66: Sistema de cadastro básico com CRUD de nomes"""
    nomes_cadastrados = []

    def cadastrar_nome():
        nome = input("Digite o nome para cadastrar: ")
        nomes_cadastrados.append(nome)
        print(f"Nome '{nome}' cadastrado com sucesso!")

    def atualizar_nome():
        listar_nomes()
        try:
            indice = int(input("Digite o número do nome para atualizar: ")) - 1
            nome_antigo = nomes_cadastrados[indice]
            nome_novo = input("Digite o novo nome: ")
            nomes_cadastrados[indice] = nome_novo
            print(f"Nome '{nome_antigo}' atualizado para '{nome_novo}'!")
        except (ValueError, IndexError):
            print("Número inválido!")

    def excluir_nome():
        listar_nomes()
        try:
            indice = int(input("Digite o número do nome para excluir: ")) - 1
            nome_excluido = nomes_cadastrados.pop(indice)
            print(f"Nome '{nome_excluido}' excluído com sucesso!")
        except (ValueError, IndexError):
            print("Número inválido!")

    def listar_nomes():
        if not nomes_cadastrados:
            print("Não há nomes cadastrados.")
        else:
            print("\n=== NOMES CADASTRADOS ===")
            for i, nome in enumerate(nomes_cadastrados, 1):
                print(f"{i}. {nome}")

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar nome")
        print("2 - Atualizar nome")
        print("3 - Excluir nome")
        print("4 - Listar nomes")
        opcao = input("Escolha uma opção (outra tecla para sair): ")

        if opcao == '1': cadastrar_nome()
        elif opcao == '2': atualizar_nome()
        elif opcao == '3': excluir_nome()
        elif opcao == '4': listar_nomes()
        else: break
        
        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != 's': break

    print("Obrigado por usar o sistema!")


def exercicio_67():
    """Exercício 67: Jogo da velha básico no terminal"""
    
    def criar_tabuleiro():
        return [[' ' for _ in range(3)] for _ in range(3)]

    def exibir_tabuleiro(tabuleiro):
        print("\n  0 1 2")
        for i, linha in enumerate(tabuleiro):
            print(f"{i} {linha[0]}|{linha[1]}|{linha[2]}")

    def verificar_vitoria(tabuleiro, jogador):
        for i in range(3):
            if all(tabuleiro[i][j] == jogador for j in range(3)): return True # Linha
            if all(tabuleiro[j][i] == jogador for j in range(3)): return True # Coluna
        if all(tabuleiro[i][i] == jogador for i in range(3)): return True # Diagonal Principal
        if all(tabuleiro[i][2-i] == jogador for i in range(3)): return True # Diagonal Secundária
        return False
    
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'
    rodadas = 0

    while rodadas < 9:
        exibir_tabuleiro(tabuleiro)
        print(f"\nVez do Jogador ({jogador_atual})")
        try:
            linha, coluna = map(int, input("Digite linha e coluna (ex: 1 2): ").split())
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador_atual
                rodadas += 1
                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"\nParabéns! Jogador '{jogador_atual}' venceu!")
                    return
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
            else:
                print("Posição já ocupada!")
        except (ValueError, IndexError):
            print("Entrada inválida!")

    exibir_tabuleiro(tabuleiro)
    print("\nEmpate!")

def exercicio_68():
    """Exercício 68: Sistema de cadastro de alunos avançado com classes e validação"""
    
    class Aluno:
        matriculas_usadas = set()
        def __init__(self, nome, email, data_nascimento):
            self.nome = nome
            self.email = email
            self.data_nascimento = data_nascimento
            self.matricula = self._gerar_matricula()
        
        def _gerar_matricula(self):
            while True:
                matricula = f"ALU{random.randint(1000, 9999)}"
                if matricula not in Aluno.matriculas_usadas:
                    Aluno.matriculas_usadas.add(matricula)
                    return matricula
        
        def __str__(self):
            return f"Matrícula: {self.matricula}\nNome: {self.nome}\nE-mail: {self.email}\nData de Nascimento: {self.data_nascimento}"

    alunos = []

    def validar_nome(nome): return bool(nome.strip() and re.match("^[a-zA-ZÀ-ÿ\s]+$", nome))
    def validar_email(email): return bool(email.strip() and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
    def validar_data(data):
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def cadastrar_aluno():
        nome = input("Nome: "); email = input("Email: "); data = input("Data de Nascimento (DD/MM/AAAA): ")
        if not validar_nome(nome): print("Nome inválido."); return
        if not validar_email(email): print("Email inválido."); return
        if not validar_data(data): print("Data inválida."); return
        
        novo_aluno = Aluno(nome, email, data)
        alunos.append(novo_aluno)
        print(f"Aluno cadastrado com sucesso! Matrícula: {novo_aluno.matricula}")
    
    def buscar_aluno_por_matricula(matricula):
        for aluno in alunos:
            if aluno.matricula == matricula.upper():
                return aluno
        return None

    def atualizar_aluno():
        matricula = input("Digite a matrícula do aluno para atualizar: ")
        aluno = buscar_aluno_por_matricula(matricula)
        if aluno:
            print("Deixe em branco para não alterar.")
            novo_nome = input(f"Novo nome ({aluno.nome}): ")
            novo_email = input(f"Novo email ({aluno.email}): ")
            nova_data = input(f"Nova data ({aluno.data_nascimento}): ")
            if novo_nome and validar_nome(novo_nome): aluno.nome = novo_nome
            if novo_email and validar_email(novo_email): aluno.email = novo_email
            if nova_data and validar_data(nova_data): aluno.data_nascimento = nova_data
            print("Aluno atualizado!")
        else:
            print("Matrícula não encontrada.")
            
    def remover_aluno():
        matricula = input("Digite a matrícula do aluno para remover: ")
        aluno = buscar_aluno_por_matricula(matricula)
        if aluno:
            alunos.remove(aluno)
            Aluno.matriculas_usadas.discard(aluno.matricula)
            print("Aluno removido!")
        else:
            print("Matrícula não encontrada.")

    def listar_alunos():
        if not alunos: print("Nenhum aluno cadastrado.")
        for aluno in alunos: print(f"\n---\n{aluno}")
            
    # Menu do exercício 68
    while True:
        print("\n=== CADASTRO DE ALUNOS ===")
        print("1-Cadastrar 2-Atualizar 3-Remover 4-Listar 5-Buscar 0-Sair")
        opcao = input("> ")
        if opcao == '1': cadastrar_aluno()
        elif opcao == '2': atualizar_aluno()
        elif opcao == '3': remover_aluno()
        elif opcao == '4': listar_alunos()
        elif opcao == '5':
            aluno = buscar_aluno_por_matricula(input("Matrícula: "))
            print(aluno if aluno else "Não encontrado.")
        elif opcao == '0': break

def exercicio_69():
    """Exercício 69: Jogo da velha melhorado com detecção de empate e nova partida"""
    
    def criar_tabuleiro(): return [[' ' for _ in range(3)] for _ in range(3)]

    def exibir_tabuleiro(tabuleiro):
        print("\n  0 1 2")
        for i, linha in enumerate(tabuleiro): print(f"{i} {linha[0]}|{linha[1]}|{linha[2]}")

    def verificar_vitoria(tab, jog):
        vitorias = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)], # Linhas
                    [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)], # Colunas
                    [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]                     # Diagonais
        for vitoria in vitorias:
            if all(tab[l][c] == jog for l, c in vitoria): return True
        return False
        
    def jogar():
        tabuleiro = criar_tabuleiro()
        jogador_atual = 'X'
        rodadas = 0
        while True:
            exibir_tabuleiro(tabuleiro)
            print(f"\nVez do Jogador ({jogador_atual})")
            try:
                linha, coluna = map(int, input("Digite linha e coluna (ex: 1 2): ").split())
                if 0 <= linha <= 2 and 0 <= coluna <= 2:
                    if tabuleiro[linha][coluna] == ' ':
                        tabuleiro[linha][coluna] = jogador_atual
                        rodadas += 1
                        if verificar_vitoria(tabuleiro, jogador_atual):
                            exibir_tabuleiro(tabuleiro)
                            print(f"\nParabéns! Jogador '{jogador_atual}' venceu!")
                            return
                        if rodadas == 9:
                            exibir_tabuleiro(tabuleiro)
                            print("\nEmpate!")
                            return
                        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
                    else:
                        print("Posição já ocupada!")
                else:
                    print("Posição inválida! Use números de 0 a 2.")
            except (ValueError, IndexError):
                print("Entrada inválida!")

    while True:
        jogar()
        if input("Jogar novamente? (s/n): ").lower() != 's':
            print("Obrigado por jogar!")
            break

# ===== MENU PRINCIPAL =====

def menu_principal():
    """Menu principal para navegação entre todos os 69 exercícios"""
    exercicios = {
        1: exercicio_01, 2: exercicio_02, 3: exercicio_03, 4: exercicio_04, 5: exercicio_05,
        6: exercicio_06, 7: exercicio_07, 8: exercicio_08, 9: exercicio_09, 10: exercicio_10,
        11: exercicio_11, 12: exercicio_12, 13: exercicio_13, 14: exercicio_14, 15: exercicio_15,
        16: exercicio_16, 17: exercicio_17, 18: exercicio_18, 19: exercicio_19, 20: exercicio_20,
        21: exercicio_21, 22: exercicio_22, 23: exercicio_23, 24: exercicio_24, 25: exercicio_25,
        26: exercicio_26, 27: exercicio_27, 28: exercicio_28, 29: exercicio_29, 30: exercicio_30,
        31: exercicio_31, 33: exercicio_33, 34: exercicio_34, 35: exercicio_35, 36: exercicio_36,
        37: exercicio_37, 38: exercicio_38, 39: exercicio_39, 40: exercicio_40, 41: exercicio_41,
        42: exercicio_42, 43: exercicio_43, 44: exercicio_44, 45: exercicio_45, 46: exercicio_46,
        47: exercicio_47, 48: exercicio_48, 49: exercicio_49, 50: exercicio_50, 51: exercicio_51,
        52: exercicio_52, 53: exercicio_53, 54: exercicio_54, 55: exercicio_55, 56: exercicio_56,
        57: exercicio_57, 58: exercicio_58, 59: exercicio_59, 60: exercicio_60, 61: exercicio_61,
        62: exercicio_62, 63: exercicio_63, 64: exercicio_64, 65: exercicio_65, 66: exercicio_66,
        67: exercicio_67, 68: exercicio_68, 69: exercicio_69
    }
    
    print("=" * 40)
    print("   LISTA COMPLETA DE EXERCÍCIOS PYTHON")
    print("=" * 40)
    
    while True:
        try:
            escolha = int(input("\nDigite o número do exercício (1-69) ou 0 para sair: "))
            
            if escolha == 0:
                print("Obrigado por usar o sistema!")
                break
            elif escolha == 32:
                print("Exercício 32 foi pulado.")
            elif escolha in exercicios:
                print(f"\n--- EXERCÍCIO {escolha} ---")
                exercicios[escolha]()
                print("-" * (18 + len(str(escolha))))
            else:
                print("Exercício inválido! Digite um número entre 1 e 69.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
        except KeyboardInterrupt:
            print("\n\nSaindo do programa...")
            break

# Ponto de entrada do programa: executa o menu principal.
if __name__ == "__main__":
    menu_principal()
