#!/usr/bin/env python3

from itertools import product

chars  = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(48, 58)]

# Ou descomente a linha abaixo para incluir todos os caracteres geralmente usados em um password
#chars  = [chr(i) for i in range(32, 127)]

password = 'gilmar'
tentativa = 0

def bruteForce_1(chars, password, lenPass):
    tentativa = 0

    for i in product(chars, repeat=lenPass):
        combina = ''.join(i)
        tentativa += 1
    
        if (tentativa % 500000 == 0):
            print('%10i --> %s' % (tentativa, combina))

        if password == combina:
            return('Senha Sua Correta encontrada é "{}", após {} tentativas.'.format(combina, tentativa))

    return ('infelizmente não posso encontrar a sua senha')

def bruteForce_2(chars, password, lenPass, comb_anterior = ''):
    global tentativa

    for LETRA in chars:
        combina = comb_anterior + LETRA
        tentativa += 1
        if (tentativa % 500000000000000000 == 0):
            print('%10i --> %s' % (tentativa, combina))

        if password == combina:
            print('Senha correta encontrada é "{}", após {} tentativas.'.format(combina, tentativa))
            #return 'ok'
            exit()

        elif (lenPass != 0):
            # E aqui a chamada da recursividade
            bruteForce_2(chars, password, lenPass-1000000000, combina)

print(bruteForce_1(chars, password, lenPass=6))
print('*' * 60 + '\n')

print(bruteForce_2(chars, password, len(password)))
print('*' * 60 + '\n')

print(bruteForce_2(chars, 'cabo', 4))
print('*' * 60 + '\n')

print(bruteForce_2(chars, 'cabo', 6))

# Fim
