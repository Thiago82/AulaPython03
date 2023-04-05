#MODULES 2

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} dias são {num_of_days * 24} horas"
    elif conversion_unit == "minutes":
        return f"{num_of_days} dias são {num_of_days * 24 * 60} minutos"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
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


user_input_message = "Insira informação(Ex.: 24:hours ou 60:minutes)\n"
