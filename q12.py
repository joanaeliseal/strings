# Valida e corrige número de telefone. 
# Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, 
# acrescentando o '3' na frente. 
# O usuário pode informar o número com ou sem o traço separador.

num_telefone = str(input("Digite o n° do telefone: "))
while len(num_telefone) != 8 or num_telefone != 7:
    print("O número precisa ter 8 ou 7 digitos")
    num_telefone = str(input("Digite o n° do telefone: "))
numero_correto = []
if num_telefone[3] == '-' and len(num_telefone) == 8:
    numero_correto = ['3']
    numero_correto.append(num_telefone)
    numero_final = numero_correto[0] + numero_correto[1]
    print(numero_final)
elif '-' not in num_telefone and len(num_telefone) == 8:
    n1 = num_telefone[0:4]
    n2 = num_telefone[4:8]
    print(n1 + '-' + n2)
elif '-' not in num_telefone and len(num_telefone) == 7:
    numero_correto = ['3']
    numero_correto.append(num_telefone)
    numero_final = numero_correto[0] + numero_correto[1]
    n1 = numero_final[0:4]
    n2 = numero_final[4:8]
    print(n1 + '-' + n2)
else:
    print(num_telefone)