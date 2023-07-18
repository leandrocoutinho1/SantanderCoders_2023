"""
Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas. De acordo com as 
perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:

Sente dor no corpo?
Você tem febre?
Você tem tosse?
Está com congestão nasal?
Tem manchas pelo corpo?

Para o diagnóstico ele tem a seguinte tabela:

A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças
Obs.: Coloque "Inconclusivo" para os casos não contemplados na tabela
"""


print("Responda as perguntas abaixo com 'Sim' ou 'Não':")

respostas = []
dor = febre = tosse = congestao_nasal = manchas = ''

while dor != 'SIM' and dor != 'NÃO':
    dor = input("Sente dor no corpo? ").upper()
    if dor != 'SIM' and dor != 'NÃO':
        print("Digite uma opção válida.")

while febre != 'SIM' and febre != 'NÃO':
    febre = input("Você tem febre? ").upper()
    if febre != 'SIM' and febre != 'NÃO':
        print("Digite uma opção válida.")

while tosse != 'SIM' and tosse != 'NÃO':
    tosse = input("Você tem tosse? ").upper()
    if tosse != 'SIM' and tosse != 'NÃO':
        print("Digite uma opção válida.")

while congestao_nasal != 'SIM' and congestao_nasal != 'NÃO':
    congestao_nasal = input("Está com congestão nasal? ").upper()
    if congestao_nasal != 'SIM' and congestao_nasal != 'NÃO':
        print("Digite uma opção válida.")

while manchas != 'SIM' and manchas != 'NÃO':
    manchas = input("Tem manchas pelo corpo? ").upper()
    if manchas != 'SIM' and manchas != 'NÃO':
        print("Digite uma opção válida.")

respostas.append(dor)
respostas.append(febre)
respostas.append(tosse)
respostas.append(congestao_nasal)
respostas.append(manchas)


if respostas == ['SIM', 'SIM', 'NÃO', 'NÃO', 'SIM']:
    print("\nDiagnóstico: Dengue")
elif respostas == ['SIM', 'SIM', 'SIM', 'SIM', 'NÃO']:
    print("\nDiagnóstico: Gripe")
elif respostas == ['NÃO', 'SIM', 'SIM', 'SIM', 'NÃO']:
    print("\nDiagnóstico: Gripe")
elif respostas == ['SIM', 'SIM', 'SIM', 'SIM', 'NÃO']:
    print("\nDiagnóstico: Gripe")
elif respostas == ['SIM', 'NÃO', 'NÃO', 'NÃO', 'NÃO']:
    print("\nDiagnóstico: Sem doenças")
elif respostas == ['NÃO', 'NÃO', 'NÃO', 'NÃO', 'NÃO']:
    print("\nDiagnóstico: Sem doenças")
else:
    print("\nDiagnóstico: Inconclusivo")

## Justificativa: Eu quis validar os casos que o usuário não não adicionava 'Sim' ou 'Não'.