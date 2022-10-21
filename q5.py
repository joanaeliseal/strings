#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

nome = input(str('Digite seu nome: ')).upper() #String em maiúscula 
for i in range(0,len(nome)+1): #variaveis iterárias!
    print(nome[i:-1])