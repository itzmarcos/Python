import os
lista = []

while True:
    print('Selecione uma opção')
    opção = input('[i]nserir', '[a]pagar', '[l]istar')
    if opção == 'i':
        nome = input('Nome: ')
        list.append(nome)
    elif opção == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite numero int.')
        except IndexError:
            print('índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opção == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para lsitar')

        for i, nome in enumerate(lista):
            print(i,nome)