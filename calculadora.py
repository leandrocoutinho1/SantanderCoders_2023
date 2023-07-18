print("__Calculadora:__")

op = ''

while op != 'S':
    op = input("\nDigite a operação matemática \n [+ - * / **] (Digite S para sair): ")
    if (op != '+') and (op != '-') and (op != '*') and (op != '/') and (op != '**') and (op != 'S'):
        print("Digite uma opção válida")
        
    else:
        if op.lower() != 's':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if op == '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            if op == '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            if op == '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            if op == '/':
                if (num1 == 0) or (num2 == 0):
                    print("Não é possível realizar divisões por 0.")
                else:
                    print(f"{num1} / {num2} = {num1 / num2 :.2f}")
            if op == '**':
                print(f"{num1} ** {num2} = {num1 ** num2 :.2f}")
            if (op != '+') and (op != '-') and (op != '*') and (op != '/') and (op != '**') and (op != 'S'):
                print("Digite uma opção válida")
        else:
            print("\nCalculadora encerrada.")
