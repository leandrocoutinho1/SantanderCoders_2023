from collections import namedtuple

Pessoa = namedtuple("Pessoa", ["nome", "idade", "sexo"])


def cadastrar_usuario():
    continuar_cadastro = True
    cadastros = []  # list(), iniciando uma lista vazia

    while continuar_cadastro:
        cadastrar = input("Deseja inserir um novo cadastro? ")
        if cadastrar.lower() in ["sim", "s", "yes", "y"]:
            nome = input("Insira o nome: ")
            idade = int(input("Insira a idade: "))
            sexo = input("Insira o sexo: ")
            cadastro = Pessoa(nome=nome, idade=idade, sexo=sexo)
            # cadastro = Pessoa(nome, idade, sexo), alternativa para cadastrar a pessoa
            cadastros.append(cadastro)
        elif cadastrar.lower() in ["não", "n", "nao", "no"]:
            print(f"Cadastro finalizado, inserido {len(cadastros)} novos")
            continuar_cadastro = False
        else:
            print(
                f'Opção invalida. Foi inserido "{cadastrar}",\
escolha entre [sim, s, yes, y] para cadastrar uma nova pessoa ou [não, nao, n, no] para parar'
            )
    return cadastros


def calcule_media_idade_por_sexo(cadastros):
    idades_m = []  # Lista para armazenar o sexo masculino
    idades_f = []  # Lista para armazenar o sexo feminino
    sexo_indefinido = 0  # Contador para cadastros de sexo incorreto ou indefinido

    for cadastro in cadastros:
        sexo = cadastro.sexo  # cadastro[2], alternativa para pegar por posição da tupla
        idade = (
            cadastro.idade
        )  # cadastro[1], alternativa para pegar por posição da tupla

        if sexo.lower() == "m":
            idades_m.append(idade)
        elif sexo.lower() == "f":
            idades_f.append(idade)
        else:
            # Incrementando o contador de sexo indefinido
            sexo_indefinido += 1

    if len(idades_m) > 0:
        media_m = sum(idades_m) / len(idades_m)
    else:
        media_m = 0

    if len(idades_f) > 0:
        media_f = sum(idades_f) / len(idades_f)
    else:
        media_f = 0

    porcentagem_indefinido = 100 * (sexo_indefinido / len(cadastros))
    print(
        f"Número de pessoas com sexo não informado {sexo_indefinido}, representando {porcentagem_indefinido:.2f}% das pessoas cadastradas"
    )
    return (("m", media_m), ("f", media_f))

cadastros = cadastrar_usuario()

print(calcule_media_idade_por_sexo(cadastros))
