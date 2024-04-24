def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    return a / b

def potencia (a,b):
    return a ** b

continuar = True

while continuar :

    x = input("escreva o primeiro numero: ")
    operacao = input("qual sera a operação matematica? ")
    y = input("escreva o segundo numero: ")

    a = float(x)
    b = float(y)

    resultado = None

    if operacao in ["potencia", "elevado", "^"]:
        resultado = potencia(a,b)
    elif operacao in ["adição", "adiçao", "mais", "+"]:
        resultado = soma(a,b)
    elif operacao in ["subtração", "subtraçao", "menos", "-"]:
        resultado = subtracao(a,b)
    elif operacao in ["vezes", "multiplicação", "*", "x"]:
        resultado = multiplicacao(a,b)
    elif operacao in ["dividido", "divisão", "divisao", "/"]:
        resultado = divisao(a,b)
    else:
        print("Erro de cálculo")
        continuar = input("Deseja fazer outra operação? (s/n): ").lower() == 's'
        continuar

    print("Resultado:", resultado)
    continuar = input("Deseja fazer outra operação? (s/n): ").lower() == 's'