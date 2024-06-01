#  def multiplicar(*args):
#      total = 1
#      for arg in args:
#         total *= arg
#     return total

# resultado = multiplicar(2, 3, 4)
# #print(f"O valor da variável resultado é: {resultado}")

# def verificar_paridade(numero):
#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "ímpar"

# numero = 9
# resultado = verificar_paridade(numero)
# print(f"O número {numero} é {resultado}.")



def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
print(duplicar(2))
print(triplicar(3))