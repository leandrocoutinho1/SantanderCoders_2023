"""
Crie um script que leia diversos números inteiros e insira todos em uma lista. A cada solicitação 
de número pergunte ao usuário se deseja inserir outro número, tendo como resposta 'S' para inserir mais um ou 'N' caso 
queira terminar. Ao final mostre:

Obs.: Números primos são aqueles que são divisíveis APENAS por 1 e por ele mesmo. Por exemplo, o número 13 
    é primo visto que só pode ser dividido por 1 e pelo próprio 13.
"""
# a) todos os números digitados na ordem em que foram inseridos

numeros = []
resposta = 'S'

while resposta != 'N':
    if resposta == 'S':
        numero = int(input('Digite um número inteiro: '))
        numeros.append(numero)
        resposta = input('Deseja inserir outro número? [S/N]: ').upper()
    if resposta != 'S' and resposta != 'N':
        print("Digite uma opção válida.")
        resposta = input('Deseja inserir outro número? [S/N]: ').upper()
print("\na) ")
print(f'Números digitados na ordem em que foram inseridos: {numeros}')


# b) todos os números digitados em ordem crescente

numeros_ord_cres = sorted(numeros)

print("\nb) ")
print(f'Números digitados em ordem crescente: {numeros_ord_cres}')


# c) a média destes valores

soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)

print("\nc) ")
print(f'Média dos valores digitados: {media}')


# d) apenas os números primos


primos = []

for numero in numeros:
    if numero >= 2:
        is_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                is_primo = False

        if is_primo == True:
            primos.append(numero)

print("\nd) ")
print(f'Números primos: {primos}')