# 1 Variáveis  e formatação

# calc_to_sec = 24 * 34 * 2
# ano = 365
# dias = str(30)
# nome_unidade = "dias"
#
# print(f"Um ano são cerca de {ano} {nome_unidade}.")
# print(f"{ano} {nome_unidade} são {ano / 30} meses.")
# print(f"Cada mês do ano possue cerca de {ano / 12} {nome_unidade}.")
#
# print(f"São cerca de {5 * calc_to_sec} segundos")
# print(f"São cerca de {10 * calc_to_sec} segundos")
# print(f"São cerca de {30 * calc_to_sec} segundos")
#
# print("Faltam "+str(40)+" dias.")
# print("Faltam "+dias+" dias.")
# print(f"Faltam {69} dias")
# print(f"Faltam {6*4%7*89} dias")

# -------------------------------------------------------------------------------------#

# # 2 Funções, "encapsular lógica".
#
# calc_to_unit = 24
# name_of_unit = "horas"
#
# def dias_para_unit(numero_de_dias, mensagem_custom): # Bloco precisa ser chamado
#      print(f"{numero_de_dias} dias são {numero_de_dias * calc_to_unit} {name_of_unit}")
#      print(mensagem_custom)
#
#  # Chamando o bloco de função
#
#  dias_para_unit(20, "Incrível!")
#  dias_para_unit(35, "Bom")]

# -------------------------------------------------------------------------------------#


# 3 Scope

# calc_to_unit = 24
# name_of_unit = "horas"
#
# def dias_para_unit(numero_de_dias, mensagem_custom): # Bloco precisa ser chamado
#       print(f"{numero_de_dias} dias são {numero_de_dias * calc_to_unit} {name_of_unit}")
#       print(mensagem_custom)
#
# def scope_check(numero_de_dias):#Numero_de_dias precisou ser colocado para variavel local funcionar
#     my_local_var = "Variavel dentro da função, torna-se variável local"
#     print(name_of_unit) #Global
#     print(numero_de_dias) #Local
#     print(my_local_var)
#
# #Aqui, numero_de_dias não funciona, pois não é global (como name_of_unit)
# scope_check(1)#Insera qualquer valor aqui para a variavel funcionar


# ----------------------------------------------------------------------------------------#

# 4 Input

# calc_to_unit = 24
# name_of_unit = "horas"
#
#
# def dias_para_unit(num_de_dias):  # Bloco precisa ser chamado
#     return f"{num_de_dias} dias são {num_de_dias * calc_to_unit} {name_of_unit}"  # retorna novamente fora da função
#
#
# my_var = dias_para_unit(20)  # Graças a return, pode ser invocado aqui como variavel
# print(my_var)
#
# user_input = input("Insira algo:\n")  # input também pode ser direcionado como variável
# print(user_input)  # Então, imprime o correto

# ----------------------------------------------------------------------------------------#

# 4 Input (Parte 2)

# calc_to_unit = 24
# name_of_unit = "horas"
#
#
# def dias_para_unit(num_de_dias):  # Bloco precisa ser chamado
#     return f"{num_de_dias} dias são {num_de_dias * calc_to_unit} {name_of_unit}"  # retorna novamente fora da função
#
#
#
# user_input = input("Insira algo:\n")  # input também pode ser direcionado como variável
# user_input_number = int(user_input) # calculando para número inteiro
#
# valor_calculado = dias_para_unit(user_input_number)  # mais variavel
# print(valor_calculado)

# ---------------------------------------------------------------------------------------- #

#  5 - Condições If/Else

# unidade = 24 #  Variavel indicando o dia (24 horas)
# nome_uni = "horas" #  Nome da unidade
#
#
# def DiaPraHora(num_de_dias): #  Função que converte dia pra horas
#     print(num_de_dias > 0) #  Boolean é impresso informando o resultado atrvaés de true or false (?????)
#     checa_condition = num_de_dias > 0 #  criando um boolean para informar a condição true/false da função
#     #type(checa_condition) #  Mostra o tipo de dado
#     print(type(checa_condition)) # Coloca então dentro do print pra vermos o resultado
#
#     if num_de_dias > 0: # Se o número inserido for maior que 0
#         return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}" # então faz o cálculo
#     else: #  caso contrário
#         return "Valor negativo, sem conversão"  #  Sem conversão se o valor for negativo
#     # Obs.: Return deve ser usado para jogar o valor pra fora da função novamente
#
#
# input_numero = input("Insira um número:\n") #  cria a caixa que permite inserir o numero
# input_valor = int(input_numero) # Este é o número, já indicando que a conversão é número inteiro
#
# #valor_calculado = DiaPraHora(input_valor) # Colocamos o resultado final numa variavel
# valor_calculado = DiaPraHora(int(input_numero)) #  Assim também vale
#
# print(valor_calculado) # E imprimimos

# -------------------------------------------------------------------------------------------#

#  5 (Parte 2)

# unidade = 24 #  Variavel indicando o dia (24 horas)
# nome_uni = "horas" #  Nome da unidade
#
#
# def DiaPraHora(num_de_dias): #  Função que converte dia pra horas
#     if num_de_dias > 0: # Se o número inserido for maior que 0
#         return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}" # então faz o cálculo
#     elif num_de_dias == 0:  # Basicamente, else + if // Se for igual a 0
#         return "Você inseriu 0 (zero)."
#     else: #  caso contrário
#         return "Valor negativo, sem conversão"  #  Sem conversão se o valor for negativo
#     # Obs.: Return deve ser usado para jogar o valor pra fora da função novamente
#
# def ValidaNumeral(): # Função criada
#     if input_numero.isdigit():  # Aqui, verificaremos se é número ou texto
#         input_valor = int(input_numero)
#         valor_calculado = DiaPraHora(int(input_numero))  # Assim também vale
#         print(valor_calculado)  # E imprimimos
#     else:
#         print("Favor, inserir um número válido para cálculo.")
#
# input_numero = input("Insira um número:\n") #  cria a caixa que permite inserir o numero
# ValidaNumeral()


# ----------------------------------------------------------------------------------------#

### 5 - Parte 3 - NESTED

# unidade = 24  # Variavel indicando o dia (24 horas)
# nome_uni = "horas"  # Nome da unidade
#
#
# def dia_pra_hora(num_de_dias):  # Função que converte dia pra horas
#     if num_de_dias > 0:  # Se o número inserido for maior que 0
#         return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}"  # então faz o cálculo
#
#
# def valida_numeral():  # Função criada para verificar númeral ou texto
#     if input_numero.isdigit():  # Usuário colocou número?
#         input_valor = int(input_numero)
#         if input_valor > 0: # É um número positivo?
#             valor_calculado = dia_pra_hora(input_valor) # Executada se a condição anterior procede
#             print(valor_calculado)  # E imprimimos
#         elif input_valor == 0:  # Ou é zero?
#             print("Você inseriu 0 (zero).") # Então informa que é zero.
#
#     else:
#         print("Favor, inserir um número válido para cálculo.") # Se não colocou numero, aparece esta mensagem
#
#
# input_numero = input("Insira um número:\n")  # cria a caixa que permite inserir o numero
# valida_numeral() # Invoca função

#----------------------------------------------------------------------------------------


# Parte 6 - Continua - TRY EXCEPT

# unidade = 24  # Variavel indicando o dia (24 horas)
# nome_uni = "horas"  # Nome da unidade
#
#
# def dia_pra_hora(num_de_dias): #  Função que converte dia pra horas
#       if num_de_dias > 0: # Se o número inserido for maior que 0
#           return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}" # então faz o cálculo
#
# def valida_numeral():  # Função criada para verificar númeral ou texto
#     try:  # TRY vai "tentar" efetuar o código de maneira exata, sem precisarmos colcoar muitas condições..."
#         usuario_input_valor = int(usuario_input)
#         if usuario_input_valor > 0: # É um número positivo?
#             valor_calculado = dia_pra_hora(usuario_input_valor) # Executada se a condição anterior procede
#             print(valor_calculado)  # E imprimimos
#         elif usuario_input_valor == 0:  # Ou é zero?
#             print("Você inseriu 0 (zero).") # Então informa que é zero.
#         else:
#             print("Você inseriu um número negativo. Tente novamente.")
#     except ValueError: # "...ENQUANTO except vai mostrar a resposta" "TRY CATCH"
#         print("Favor, inserir um número válido para cálculo.") # Se não colocou numero, aparece esta mensagem
#
#
# usuario_input = input("Insira um número:\n")  # cria a caixa que permite inserir o numero
# valida_numeral() # Invoca função

#-----------------------------------------------------------------------------------------------


# Parte 7 - WHILE LOOP

# unidade = 24  # Variavel indicando o dia (24 horas)
# nome_uni = "horas"  # Nome da unidade
#
#
# def dia_pra_hora(num_de_dias): #  Função que converte dia pra horas
#       if num_de_dias > 0: # Se o número inserido for maior que 0
#           return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}" # então faz o cálculo
#
# def valida_numeral():  # Função criada para verificar númeral ou texto
#     try:  # TRY vai "tentar" efetuar o código de maneira exata, sem precisarmos colcoar muitas condições..."
#         usuario_input_valor = int(usuario_input)
#         if usuario_input_valor > 0: # É um número positivo?
#             valor_calculado = dia_pra_hora(usuario_input_valor) # Executada se a condição anterior procede
#             print(valor_calculado)  # E imprimimos
#         elif usuario_input_valor == 0:  # Ou é zero?
#             print("Você inseriu 0 (zero).") # Então informa que é zero.
#         else:
#             print("Você inseriu um número negativo. Tente novamente.")
#     except ValueError: # "...ENQUANTO except vai mostrar a resposta" "TRY CATCH"
#         print("Favor, inserir um número válido para cálculo.") # Se não colocou numero, aparece esta mensagem
#
# ## ABAIXO:while permite a operação inteira continuar ativa
# usuario_input = ""
# while usuario_input != "exit":  #  while True: Executa várias coisas enquanto a condição é ativa
#     usuario_input = input("Insira um número:\n")  # cria a caixa que permite inserir o numero
#     valida_numeral() # Invoca função

#---------------------------------------------------------------------------------------------------#

# Parte 8 -  Lista e For Loops

unidade = 24  # Variavel indicando o dia (24 horas)
nome_uni = "horas"  # Nome da unidade


def dia_pra_hora(num_de_dias): #  Função que converte dia pra horas
      if num_de_dias > 0: # Se o número inserido for maior que 0
          return f"{num_de_dias} dias são {num_de_dias * unidade} {nome_uni}" # então faz o cálculo

def valida_numeral():  # Função criada para verificar númeral ou texto
    try:  # TRY vai "tentar" efetuar o código de maneira exata, sem precisarmos colcoar muitas condições..."
        usuario_input_valor = int(num_de_dias_element) # LISTA?
        if usuario_input_valor > 0: # É um número positivo?
            valor_calculado = dia_pra_hora(usuario_input_valor) # Executada se a condição anterior procede
            print(valor_calculado)  # E imprimimos
        elif usuario_input_valor == 0:  # Ou é zero?
            print("Você inseriu 0 (zero).") # Então informa que é zero.
        else:
            print("Você inseriu um número negativo. Tente novamente.")
    except ValueError: # "...ENQUANTO except vai mostrar a resposta" "TRY CATCH"
        print("Favor, inserir um número válido para cálculo.") # Se não colocou numero, aparece esta mensagem

## ABAIXO:while permite a operação inteira continuar ativa
usuario_input = ""
while usuario_input != "exit":  #  while True: Executa várias coisas enquanto a condição é ativa
    usuario_input = input("Insira um valor:\n")  # cria a caixa que permite inserir o numero
    print(type(usuario_input.split(", ")))
    print(usuario_input.split(", "))
    for num_de_dias_element in usuario_input.split(", "): # FOR LOOP .split tem haver com a lista
        valida_numeral() # Invoca função
