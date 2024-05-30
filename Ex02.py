#  def multiplicar(*args):
#      total = 1
#      for arg in args:
#         total *= arg
#     return total

# resultado = multiplicar(2, 3, 4)
# #print(f"O valor da variável resultado é: {resultado}")

def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = 9
resultado = verificar_paridade(numero)
print(f"O número {numero} é {resultado}.")
