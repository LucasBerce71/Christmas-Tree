from random import randint
from time import sleep

rmd2 = randint(1,30)

def gentree():
    print('\033c')
    for x in range(1,23):
        rmd1 = randint(1,rmd2)
        if x == 1:
            ch = "$"
        elif rmd1%4==0:
            ch = "o"
        elif rmd1%3==0:
            ch = "i"
        else:
            ch = "*"
        print("{:^33}".format(ch*x))
    sleep(.75)

print('Deseja receber sua árvore de natal? (s ou n)')
christmas = input()
if christmas == "s":
    gentree()
else:
    print('Obrigado por participar!')
