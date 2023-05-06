from Helisi_Responde import Responda
from cores import *


def Separa_str(s):

    # Inicializando as listas que irão armazenar os números e sinais
    numeros = []
    sinais = []

    # Inicializando uma string vazia para armazenar o número atual sendo analisado
    num_atual = ''

    # Iterando sobre cada caractere na string de entrada
    for caractere in s:

        # Se o caractere for um dígito, ele é adicionado à string num_atual
        if caractere.isdigit():
            num_atual += caractere

        # Se o caractere for um sinal matemático, o número atual é adicionado à lista de números,
        # a string num_atual é reiniciada, e o sinal é adicionado à lista de sinais
        elif caractere in ['+', '-', '*', '/', '%']:
            numeros.append(num_atual)
            num_atual = ''
            sinais.append(caractere)

    # Adicionando o último número atual à lista de números, pois não haverá mais sinais após ele
    numeros.append(num_atual)

    # Concatenando os números e sinais em uma string, na ordem em que aparecem na lista
    expressao = ''
    for i in range(len(numeros)):
        expressao += numeros[i]
        if i < len(sinais):
            expressao += sinais[i]

    # Imprimindo a expressão final
    return  expressao # resultado: '5 + 7 - 20'


def calcular(s):
    print(ciano('-------------------------------- Calculando!'))
    # Inicializa as listas vazias para guardar os números e operadores
    numeros = []
    operadores = []
    num_atual = '' # Inicializa uma string vazia para construir o número atual

    # Percorre todos os caracteres da string `s`
    for caractere in s:
        if caractere.isdigit(): # Verifica se o caractere é um dígito
            num_atual += caractere # Adiciona o dígito à string `num_atual`
        elif caractere in ['+', '-', '*', '/', '%']: # Verifica se o caractere é um operador
            numeros.append(int(num_atual)) # Converte a string `num_atual` em um número inteiro e adiciona à lista `numeros`
            num_atual = '' # Reseta a string `num_atual` para começar a construir um novo número
            operadores.append(caractere) # Adiciona o operador à lista `operadores`
    numeros.append(int(num_atual)) # Adiciona o último número construído à lista `numeros`

    # Percorre todos os operadores da lista `operadores` e realiza as operações correspondentes
    for i in range(len(operadores)):
        op = operadores[i]
        if op == '*': # Multiplicação
            resultado = numeros[i] * numeros[i+1]
        elif op == '/': # Divisão
            resultado = numeros[i] / numeros[i+1]
        elif op == '+': # Adição
            resultado = numeros[i] + numeros[i+1]
        elif op == '-': # Subtração
            resultado = numeros[i] - numeros[i+1]
        elif op == '%': # Módulo
            resultado = numeros[i] % numeros[i+1]
        numeros[i+1] = resultado # Atualiza o número na lista `numeros`

    resp =  str(numeros[-1]) # Converte o resultado final em uma string e retorna
    Responda(Separa_str(s) +" = "+ resp)
