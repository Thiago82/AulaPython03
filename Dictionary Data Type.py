# DICTIONARY DATA TYPE
# USADOS para guardar valor em pares "key:value", ou "chave:valor"
# NÂO PERMITEM valores duplicados, pois é uma coleção


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} dias são {num_of_days * 24} horas"
    elif conversion_unit == "minutes":
        return f"{num_of_days} dias são {num_of_days * 24 * 60} minutos"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("Você inseriu 0, insira um valor positivo.")
        else:
            print("Você inseriu um valor negativo.")
    except ValueError:
        print("Informação inválida")


user_input = ""
while user_input != "exit":
    user_input = input("Insira informação(Ex.: 24:hours ou 60:minutes)\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()


# my_list = ["20", "30", "100"]
# print(my_list[2])
#
# my_dictionary = {"days": 20, "unit": "hours", "message": "all good"}
# print(my_dictionary["unit"])

# message = "enter value"
# days = 20
# price = 9.99
# valid_number = True
# exit_input = False
# list_of_days = [20, 20, 20, 100]
# list_of_months = ["Janeiro", "Fevereiro, Junho"]
# set_of_days = {20, 45, 100}
# days_and_unit = {"days": 10, "unit": "hours"}