import os
os.system('cls')
import time

soma_pares = 0
quantidade_numeros = 0
quantidade_pares = 0
quantidade_ímapares = 0

while True:
    os.system('cls')
    numero = int(input('digite um número: '))

    if numero >= 0:
        quantidade_numeros += 1
        soma_geral += numero

    if numero % 2 == 0:
        quantidades_pares +=1
        soma_pares +=1
    else:
        break

    if quantidade_numeros == 0:
    print('Não foi possível calcular \n')
    else:
        media_geral = soma_pares / quantidade_numeros
        media_pares = soma_pares / quantidade_pares

    print(f'média geral:{media_geral}')
    print(f'média pares {media_pares}')
    print(f'quantidade de pares {quantidade_pares}')
    print(f'quantidade de impares {quantidade_ímpres}')