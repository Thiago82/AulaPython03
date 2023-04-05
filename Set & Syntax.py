# SET & SYNTAX

# Não possuem ordem definida!
# Não possuem referência index!
# Não podem ser mudados. Só adicionar ou remover

# lst_meses2 = ("Janeiro", "Fevereiro", "Março")
lst_meses = {"Janeiro", "Fevereiro", "Março"}

for conteudo in lst_meses:
     print(conteudo)

lst_meses.add("Abril")
print(lst_meses)

lst_meses.remove("Janeiro")
print(lst_meses)

#--------------------------------------------------