# entrada = int(input('Digite um numero INTEIRO: '))
# try:
#    # num_int = float(num)
#     if entrada % 2 == 0:
#         print('Esse numero é PAR.')
#     else:
#         print('Esse numero é IMPAR.')
# except:
#     print('Você não digitou nada! tente novamente.')

# while True:
#     try:
#         hora = int(input('Digite a hora atual: '))
#         if hora >= 0 and hora <=11:
#             print('Bom dia')
#         elif hora >= 12 and hora <= 17:
#             print('Boa tarde!')
#         elif hora >= 18 and hora <= 23:
#             print('Boa Noite! ')
#         else:
#             print('Não conheco essa hora')  
#     except:
#         print('Por favor digite a hora certa')

# for nome in range(5):
#     nome = str(input('Digite seu primeiro nome: '))
#     qts = len(nome)
#     if qts <= 1:
#         print('Por favor digite mais de uma letra')
#     elif qts <= 4:
#         print('Seu nome é curto.')
#     elif qts >= 5 and qts <= 6:
#         print('Seu nome é normal!')
#     else:
#         print('Seu nome é muito grande!')
# lista = ['Maria', 'Lucas', 1,2,3, 'Eduarda']
# print(*lista)

# SET

# l1 = [1, 2, 3, 3, 3, 3, 1]
# s1 = set(l1)
# s1 = {1, 2, 3}
# print(s1)
# print(2 in s1)

# s1 = set()
# s1.add('Ana')
# s1.update(('Olá', 1, 2, 3))
# # s1.clear()
# s1.discard(2)
# print(s1)

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2
# print(s3)

# letras = set()
# while True:
#     letra = input('Digite: ')
#     letras.add(letra.lower())

#     if 'b' in letras:
#         print('Good!')
#         break
#     print(letras)

# LAMBDA

lista = [ {'nome' : 'Luiz', 'sobrenome' : 'Carlo' },
         {'nome' : 'Ana', 'sobrenome' : 'Paula'}
         ]
def exibir(lista):
    for item in lista:
        print(item)
        print()
l1 = sorted(lista, key=lambda item: item ['nome'])
l2 = sorted(lista, key=lambda item: item ['sobrenome'])

exibir(l1)
exibir(l2)

