tentativas = 0
perguntas = [
    {
        'Pergunta' : 'Quanto é a metade de 2 + 2',
        'Opcoes' : ['1', '2', '3', '4'],
    },
    {
        'Pergunta' : 'Quanto é 120*2',
        'Opcoes' : ['25', '240', '300', '140'],
    },]
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes):
        print (f'{i})', opcao)
    print()

    escolha = input('Escolha uma opcao: ')

    acertou = False
    escolha_int = None
    quantidade_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < quantidade_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

    print()
print(f'Você acertou, com {qtd_acertos} vezes')



        