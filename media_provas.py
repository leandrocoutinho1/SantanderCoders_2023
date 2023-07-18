"""
Faça um programa que peça para o usuário digitar o nome, a idade e o número de provas que esse aluno fez. 
Depois, o programa deve pedir para o usuário digitar as notas de cada prova do aluno. Ao final, o programa deve 
imprimir uma lista contendo:
"""

# a) Nome do aluno na posição 0 

nome = input("Digite o nome do aluno: ")
idade = input("Digite a idade do aluno: ")
num_provas = int(input("Digite o número de provas feitas pelo aluno: "))


soma = 0
lista_notas = []

for i in range(1, num_provas + 1):
    lista_notas.append(input(f"Digite a nota da prova {i}: "))


for nota in lista_notas:
    soma += float(nota)

media = soma / len(lista_notas)

maior_que_5 = media > 5

lista_aluno = [nome, idade, lista_notas, media, maior_que_5]

print("\na) ")
print(f"Nome do aluno: {lista_aluno[0]}")


# b) Idade do aluno na posição 1 

print("\nb) ")
print(f"Idade do aluno: {lista_aluno[1]}")


# c) Uma lista com todas as notas na posição 2 

print("\nc) ")
print(f"Lista com as notas do aluno: {lista_aluno[2]}")


# d) A média do aluno na posição 3 

print("\nd) ")
print(f"Média do aluno: {lista_aluno[3]}")


# e) True ou False, caso a média seja maior que 5 ou não, na posição 4

print("\ne) ")
print(f"Média do aluno maior que 5? {lista_aluno[4]}")
