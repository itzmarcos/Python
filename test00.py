
perguntas = [
    {
        'Pergunta 1' : 'Quanto é a metade de 2 + 2',
        'Opções' : ['1', '2', '3', '4'],
    },
    {
        'Pergunta 2' : 'Quanto é 120*2',
        'Opções' : ['25', '240', '300', '140'],
    },]
print(perguntas)
resposta = input('Qual sua resposta: ')
if resposta == '3':
    print('Parabéns você acertou!')
else:
    print('Você errou')