import  os
os.system('cls')
import time

while True:
    os.system('cls')
    print('''
    === MENU ===
    1 - Adicionar pessoa
    2 - Exibir resultados
    3 - Sair
    ''')
    opção = int(input('Digite a opção desejada: '))
    match opção:
        case 1:
            print('=== CADASTRO ===')
            idade = input(' Digite sua idade: ')
            sexo = input( ' Digite o sexo (M/F)').upper()
            salario = float(input('Digite seu salário\: '))

            soma_salario += salario
            contador_pessoas += 1
            maior_idade = max(idade, maior _idade)
            menor_idade = min(idade, menor_idade)

            if sexo == 'F' and salario >= 5000:
                mulheres_5k += 1

                print('pessoa adicionada com sucesso!')
                input('Pressione uma tecla para continuar...')
        case 2:
            if contador_pessoas == 0:
                print('\n nenhuma pessoa cadastrada \n')
            else:
                media_salario = soma_salario / contador_pessoas

                print('|n ==== RESULTADO DA PESQUISA ====')
                print(f'media de salario do grupo {media_salario}')
                print(f'Maior idade: {maior_idade}')
                print(f'Menor idade: {menor_idade}')
                print(f'Mulheres com salario a partir de R$ 5.000,00{mulheres_5k}')
                input('pressione para conrinuar...')
                case 3:
                    print('programa encerrado')
                    break
                case :
                    print('opção invalida \n')
                    input('pressione para continuar')