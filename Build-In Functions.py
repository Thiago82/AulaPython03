# BUILD IN FUNCTIONS exemplos

# print() >> Imprime
# input() >> Permite input
# set() >> Lista random
# int() >> transforma em inteiro
# str() >> transforma em string


# unidade = 24
# nome_uni = "horas"
#
#
# def dia_pra_hora(num_de_dias):
#         if num_de_dias > 0:
#             return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}"
#
#
# def valida_numeral():
#     try:
#         usuario_input_valor = int(num_de_dias_element)
#         if usuario_input_valor > 0:
#             valor_calculado = dia_pra_hora(usuario_input_valor)
#             print(valor_calculado)
#         elif usuario_input_valor == 0:
#             print("Você inseriu 0 (zero).")
#         else:
#             print("Você inseriu um número negativo. Tente novamente.")
#     except ValueError:
#         print("Favor, inserir um número válido para cálculo.")
#
#
#
# usuario_input = ""
# while usuario_input != "exit":
#     usuario_input = input("Insira um valor:\n")
#     var_lista_final = usuario_input.split(", ") # Variavel pra cerregar o resultado
#     for num_de_dias_element in set(usuario_input.split(", ")): # AQUI
#         valida_numeral()


# BUILD IN FUNCTIONS exemplos

# print() >> Imprime
# input() >> Permite input
# set() >> Lista random
# int() >> transforma em inteiro
# str() >> transforma em string


print("Imprime esta frase")
print(input("Impresse esse input: "))
print(set([0, 1, 3, 4, 5]))
print(int("100"))
print(str(100))


# Abaixo, chama função dretamente no valor
# Porém, cada type possue seus tipos
# int é um, str são outros, etc

"1, 2, 3".split()

[0, 1, 3, 4, 5].count()

