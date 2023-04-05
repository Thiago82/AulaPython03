# Como criar listas
# Lista possuem index, começam com 0 ZER0

# my_lista = ["1", "2", "3", "Janeiro", "Fevereiro", "Março"]  # Separar as informações
#
# print(my_lista[4])  # Imprime o index
#
# my_lista.append("Abril")  # Insere a continuação de um dado na lista
#
# print(my_lista)  # Finalmente, imprime a lista com o dado adicionado

#-----------------------------------------------------------------------#

# SET é similar, porém não carrega valores duplicados como a lista:

# Não possuem ordem definida!
# Não possuem referência index!
# Não podem ser mudados. Só adicionar ou remover

unidade = 24
nome_uni = "horas"


def dia_pra_hora(num_de_dias):
        if num_de_dias > 0:
            return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}"


def valida_numeral():
    try:
        usuario_input_valor = int(num_de_dias_element)
        if usuario_input_valor > 0:
            valor_calculado = dia_pra_hora(usuario_input_valor)
            print(valor_calculado)
        elif usuario_input_valor == 0:
            print("Você inseriu 0 (zero).")
        else:
            print("Você inseriu um número negativo. Tente novamente.")
    except ValueError:
        print("Favor, inserir um número válido para cálculo.")



usuario_input = ""
while usuario_input != "exit":
    usuario_input = input("Insira um valor:\n")
    var_lista_final = usuario_input.split(", ") # Variavel pra cerregar o resultado
    print(var_lista_final) # Aqui imprimimos uma lista, ao inves de chamar usuario em tudo
    print(set(var_lista_final)) # Aqui imprimimos uma lista

    print(type(var_lista_final)) # Aqui imprimimos o type
    print(type(set(var_lista_final))) # Aqui imprimimos o type

    for num_de_dias_element in set(usuario_input.split(", ")): # AQUI
        valida_numeral()