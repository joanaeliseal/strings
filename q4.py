# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

nome = input(str('Digite seu nome: ')).upper() #String em maiúscula 
for i in range(0, len(nome)+1): #variaveis iterárias!
    print(nome[:i])