
# VARIAVEIS = CAIXINHA COM NOME QUE GUARDA UM VALOR 
'''
ETAPA: ESTRADA
QUAL A LOGICA DA CALCULADORA? 
PRECISA DE VALORES (NUMEROS)
ENTRADA:
O USUARIOS PRECISA DIGITAR DOIS NUMEROS OU MAIS 
USUARIO PRECISA FALAR QUAL OPERAÇÃO DESAJA FAZER 

ETAPA PROCESSAMENTO:
REALIZAR AS MATEMATICAS (+, -, *, /)

ETAPA SAIDA:
EXIBIR O RESULTADO PARA O USUARIO

'''
print("===Bem vindo a calculadora do Senac === ")

primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))
operacao = input("Digite a operação que deseja realizar: ")



match operacao:
    case "+":
        resultado = float(primeiro_numero) + float(segundo_numero)
        print(resultado)
    case "-":
        resultado = float(primeiro_numero) - float(segundo_numero)
        print(resultado)
    case "*":
        resultado = float(primeiro_numero) * float(segundo_numero)
        print(resultado)
    case "/":
        if segundo_numero == 0:
            print("Erro: Divisão por zero não é permitida!!.")
        else:
            resultado = float(primeiro_numero) / float(segundo_numero)
        print(resultado) 
    case _:
        print("Operação inválida")