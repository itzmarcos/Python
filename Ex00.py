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
lista = ['Maria', 'Lucas', 1,2,3, 'Eduarda']

print(*lista)