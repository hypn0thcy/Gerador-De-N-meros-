import os
import random
from time import sleep

logo = r"""

                 ____                    _            
                / ___| ___ _ __ __ _  __| | ___  _ __ 
               | |  _ / _ \ '__/ _` |/ _` |/ _ \| '__|
               | |_| |  __/ | | (_| | (_| | (_) | |   
                \____|\___|_|  \__,_|\__,_|\___/|_|                               
                  / |/ /_ ____ _  ___ _______  ___
                 /    / // /  ' \/ -_) __/ _ \(_-<
                /_/|_/\_,_/_/_/_/\__/_/  \___/___/
                       @Created BY: hypn0thcy

"""

ln = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

os.system('cls')
print(logo)
decis = str(input("Deseja Inserir Um DDD? (s/n) -> ")).strip()
try:
    if decis.lower() == 's':
        os.system("cls")
        print(logo)
        ddd = str(input("Insira o DDD -> ")).strip()
        qntdd = int(input('Insira a Quantidade De Numeros à gerar -> '))
        with open('Resultado.txt', 'w') as escrever1:
            for x in range(0, qntdd):
                nn1 = random.choice(ln)
                nn2 = random.choice(ln)
                nn3 = random.choice(ln)
                nn4 = random.choice(ln)
                nn5 = random.choice(ln)
                nn6 = random.choice(ln)
                nn7 = random.choice(ln)
                nn8 = random.choice(ln)
                escrever1.write(f'({ddd}) 9{nn1}{nn2}{nn3}{nn4}{nn5}{nn6}{nn7}{nn8}' + '\n')
            print('')
            print('                [...]   GERANDO!!!   [...]')
            sleep(2)
            print(" Sucesso! Os Resultado Foram Escritos em 'Resultado.txt'! ")
            print('')
            input("            Pressione ENTER Para Finalizar!")
            exit()

    elif decis.lower() == 'n':
        os.system("cls")
        print(logo)
        with open('Resultado2.txt', 'w') as escrever2:
            for x in range(10, 100):
                for y in range(0, 900):
                    n1 = random.choice(ln)
                    n2 = random.choice(ln)
                    n3 = random.choice(ln)
                    n4 = random.choice(ln)
                    n5 = random.choice(ln)
                    n6 = random.choice(ln)
                    n7 = random.choice(ln)
                    n8 = random.choice(ln)
                    escrever2.write(f"({x}) 9{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}" + '\n')
            print('')
            print('                [...]   GERANDO!!!   [...]')
            sleep(2)
            print(" Sucesso! Os Resultado Foram Escritos em 'Resultado2.txt'! ")
            print('')
            input("            Pressione ENTER Para Finalizar!")
            exit()
    else:
        os.system('cls')
        print(logo)
        print('            ERROR! Por Favor Digite apenas "s" ou "n" !!!')
        print('')
        input("                   Pressione ENTER Para Finalizar!")
        exit()

except KeyboardInterrupt:
    os.system('cls')
    print(logo)
    input("\n    Pressione Enter Para Fechar! ")
    exit()
except Exception as yyyy:
    os.system('cls')
    print(logo)
    print("\n Houve Algum ERRO CRÍTICO! -> {}".format(yyyy))
    input("\n   Pressione Enter Para Fechar! ")
    exit()
