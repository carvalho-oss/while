import os
os.system('cls')

soma = 0
quantidade_notas = 0

while True:
    os.system('cls')
    print('''
    === MENU ===
    s - inserir uma nota
    n - calcular média aritimética
    ''')

    respota = input('Deseja inserir uma nota? ').lower()

    match resposta:
        case "s":
            nota = float(input('Digite uma nota:'))
            soma += nota
            quantidade_notas += 1
        case "n":
            if quantidade_notas == 0:
                print('Não foram inseridas notas \n')
                break

        case _:
            print('Opção incalidas \n')
            input('Pressione uma tecla para continuar...')
            
if quantidade_notas == 0:
    print ('Não foi inserido  as notas')
else:
    média = soma / quantidade_notas