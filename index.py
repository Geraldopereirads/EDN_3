def menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Classificar Idade")
    print("2 - Calcular IMC")
    print("3 - Converter Temperatura")
    print("4 - Verificar Ano Bissexto")
    print("0 - Sair")


def classificar_idade():
    try:
        idade = int(input("Informe sua idade: "))
        if idade < 0:
            print("Idade inválida. Digite um valor positivo.")
        elif idade <= 12:
            print("Classificação: Criança")
        elif idade <= 17:
            print("Classificação: Adolescente")
        elif idade <= 59:
            print("Classificação: Adulto")
        else:
            print("Classificação: Idoso")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


def calcular_imc():
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser maiores que zero.")
            return

        imc = peso / (altura**2)
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso normal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        else:
            print("Classificação: Obeso")
    except ValueError:
        print("Erro: Digite apenas números válidos.")


def converter_temperatura():
    try:
        temp = float(input("Digite a temperatura: "))
        origem = input("Unidade de origem (C/F/K): ").strip().upper()
        destino = input("Unidade de destino (C/F/K): ").strip().upper()

        if origem == destino:
            print(f"A temperatura permanece a mesma: {temp:.2f}°{destino}")
            return

        # Converter para Celsius
        if origem == "F":
            celsius = (temp - 32) * 5 / 9
        elif origem == "K":
            celsius = temp - 273.15
        elif origem == "C":
            celsius = temp
        else:
            print("Unidade de origem inválida.")
            return

        # Converter de Celsius para destino
        if destino == "C":
            convertido = celsius
        elif destino == "F":
            convertido = (celsius * 9 / 5) + 32
        elif destino == "K":
            convertido = celsius + 273.15
        else:
            print("Unidade de destino inválida.")
            return

        print(f"Temperatura convertida: {convertido:.2f}°{destino}")
    except ValueError:
        print("Erro: Digite valores numéricos válidos.")


def verificar_bissexto():
    try:
        ano = int(input("Digite o ano: "))

        if ano < 0:
            print("Ano inválido. Digite um valor positivo.")
            return

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    except ValueError:
        print("Digite um número inteiro válido.")


# Execução principal
while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        classificar_idade()
    elif escolha == "2":
        calcular_imc()
    elif escolha == "3":
        converter_temperatura()
    elif escolha == "4":
        verificar_bissexto()
    elif escolha == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
